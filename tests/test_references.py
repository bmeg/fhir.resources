import importlib
import inspect
from collections import defaultdict
import pathlib
from dataclasses import dataclass
from typing import List, Optional
import networkx as nx
import csv

import inflection

from fhir.resources.reference import Reference
from fhir.resources.researchsubject import ResearchSubject


@dataclass
class EdgeInfo:
    dst_name: str
    """Destination Vertex"""
    src_name: str
    """Source Vertex"""
    src_property: str
    """Source property"""
    src_parent: Optional[str] = None
    """Parent of src_property"""
    backref: Optional[str] = None
    """Suggested backref"""


def _collect_backref():
    """Traverse the schemas for all fhir classes, create a dict of edges."""
    # load all the generated classes
    submodules = sorted([fn.stem for fn in pathlib.Path('fhir/resources').glob('*.py') if not fn.stem.startswith('_')])
    edges = []
    for submodule in submodules:
        m = importlib.import_module(f'fhir.resources.{submodule}')
        for name, klass in inspect.getmembers(m):
            if inspect.isclass(klass) and klass.__module__.startswith('fhir'):
                if not hasattr(klass, '__fields__'):
                    continue
                for k, v in klass.__fields__.items():
                    if 'backref' in v.field_info.extra:
                        for enum_reference_type in set(v.field_info.extra['enum_reference_types']):
                            edge_info = EdgeInfo(**{
                                'dst_name': enum_reference_type,
                                'src_name': klass.__name__,
                                'src_property': k,
                                'src_parent': v.field_info.extra.get('parent_name', None),
                                'backref': v.field_info.extra.get('backref', None),
                            })
                            edges.append(edge_info)
    return edges


@dataclass
class BackRefAnalysis:
    destinations: List[str]
    """Unique list of destination vertex names."""

    sources: List[str]
    """Unique list of source vertex names."""

    edges: List[EdgeInfo]
    """Unique list of source vertex names."""


def _analyze_backrefs(backrefs: List[EdgeInfo]) -> BackRefAnalysis:
    sources = []
    edges = []
    destinations = []
    for edge in backrefs:
        sources.append(edge.src_name)
        destinations.append(edge.dst_name)
        edges.append(edge)
    sources = sorted(set(sources))
    destinations = sorted(set(destinations))

    return BackRefAnalysis(
        destinations=destinations,
        sources=sources,
        edges=edges,
    )


def test_collect_backrefs():
    """Ensure we can collect backrefs."""
    backrefs = _collect_backref()
    assert backrefs


def test_analyze_backrefs():
    analysis = _analyze_backrefs(_collect_backref())
    assert analysis
    assert len(analysis.destinations) == 114, "Expected lots of Destinations"
    assert len(analysis.sources) == 338, "Expected even more Sources"
    assert len(analysis.edges) == 1689, "Expected even more Sources"

    # create cytoscape files
    with open('edges.sif.src2target.tsv', 'w', newline='') as tsv_file:
        writer = csv.writer(tsv_file, delimiter='\t', lineterminator='\n')
        writer.writerow(['sourceName', '(edgeType)', 'targetName'])
        for edge in analysis.edges:
            writer.writerow([edge.src_name, edge.src_property, edge.dst_name])  # _{edge['backref']}

    collisions = defaultdict(int)
    for edge in analysis.edges:
        collisions[f"{edge.dst_name}/{edge.src_name}"] += 1

    with open('edges.sif.target2src.tsv', 'w', newline='') as tsv_file:
        writer = csv.writer(tsv_file, delimiter='\t', lineterminator='\n')
        writer.writerow(['sourceName', '(edgeType)', 'targetName'])
        for edge in analysis.edges:
            edge_name = inflection.underscore(edge.src_name)
            if collisions[f"{edge.dst_name}/{edge.src_name}"] > 1:
                edge_name = f"{edge.src_property}_{edge_name}"
            writer.writerow([edge.dst_name, edge_name, edge.src_name])

    with open('edges.sif.combined.tsv', 'w', newline='') as tsv_file:
        writer = csv.writer(tsv_file, delimiter='\t', lineterminator='\n')
        writer.writerow(['sourceName', '(edgeType)', 'targetName'])
        for edge in analysis.edges:
            edge_name = inflection.underscore(edge.src_name)
            if collisions[f"{edge.dst_name}/{edge.src_name}"] > 1:
                edge_name = f"{edge.src_property}_{edge_name}"
            writer.writerow([edge.dst_name, edge_name, edge.src_name])

        for edge in analysis.edges:
            writer.writerow([edge.src_name, edge.src_property, edge.dst_name])  # _{edge['backref']}


def test_uniq_backref():
    """Examine all classes, ensure that all backrefs are unique.
    fhir-parser/templates/template-resource.jinja2:94
    # unique but ugly: from source's point of view: field's parent name flattened and in snake_case contcatened with fields' name
	    `backref="{{ prop.parent_name|replace(".","_")|underscore}}_{{ prop.name }}"`
    # most readable: but a) causes collisions and b) rest of fhir's properties that are lists are singular
	    `backref="{{ prop.parent_name|replace(".","_")|underscore}}_{{ prop.name }}"`
    # readable: but a) causes collisions
	    `backref="{{ prop.parent_name|replace(".","_")|underscore}}"`
    """
    # fhir_resources = importlib.import_module('fhir.resources')
    print()
    submodules = sorted([fn.stem for fn in pathlib.Path('fhir/resources').glob('*.py') if not fn.stem.startswith('_')])
    backrefs = defaultdict(dict)
    for submodule in submodules:
        m = importlib.import_module(f'fhir.resources.{submodule}')
        for name, klass in inspect.getmembers(m):
            if inspect.isclass(klass) and klass.__module__.startswith('fhir'):
                if not hasattr(klass, '__fields__'):
                    continue
                for k, v in klass.__fields__.items():
                    if 'backref' in v.field_info.extra:
                        for enum_reference_type in set(v.field_info.extra['enum_reference_types']):
                            backref = v.field_info.extra['backref']
                            if v.field_info.extra['backref'] not in backrefs[enum_reference_type]:
                                backrefs[enum_reference_type][backref] = []
                            assert backref not in backrefs[enum_reference_type][backref], (
                                    'backref collision!', 'destination',
                                    f"{enum_reference_type}.{v.field_info.extra['backref']}", 'source',
                                    backref, k
                            )
                            backrefs[enum_reference_type][backref].append(backref)
                            # print('destination', f"{enum_reference_type}.{v.field_info.extra['backref']}", 'source',
                            #       backref, k)


def test_serialize_all_references():
    """Extract all references."""

    orig_dict = Reference.dict

    my_links = []

    def my_dict(self: Reference, *args, **kwargs):
        """Render a `link`, then call the original dict function."""
        parts = self.reference.split('/')
        dst_id = parts[-1]
        dst_name = inflection.underscore(parts[0])
        backref = kwargs['field'].field_info.extra['backref']
        my_links.append({"dst_id": dst_id, "dst_name": dst_name, "label": dst_name, "backref": backref})
        return orig_dict(self, *args, **kwargs)

    # patch all references
    Reference.dict = my_dict

    rs = ResearchSubject(id="foo", status="on-study", individual=Reference(reference="Patient/1"),
                         study=Reference(reference="Study/1"))

    # trigger a traversal
    rs.dict()

    # restore the original method
    Reference.dict = orig_dict

    # validate
    assert len(my_links) == 2

    for link in my_links:
        for k in ["dst_id", "dst_name", "label", "backref"]:
            assert k in link, f"Expected {k}"
        if link['backref']:
            assert '.' not in link['backref']
