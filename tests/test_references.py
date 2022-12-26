import importlib
import inspect
from collections import defaultdict
import pathlib

import inflection

from fhir.resources.reference import Reference
from fhir.resources.researchsubject import ResearchSubject


def test_uniq_backref():
    """Examine all classes, ensure that all backrefs are unique."""
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
