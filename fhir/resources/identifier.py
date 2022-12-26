# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Identifier
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic import Field

from . import element, fhirtypes


class Identifier(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An identifier intended for computation.
    An identifier - identifies some entity uniquely and unambiguously.
    Typically this is used for business identifiers.
    """

    resource_type = Field("Identifier", const=True)

    assigner: fhirtypes.ReferenceType = Field(
        None,
        alias="assigner",
        title="Organization that issued id (may be just text)",
        description="Organization that issued/manages the identifier.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
        backref="identifier_assigner",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Time period when id is/was valid for use",
        description="Time period during which identifier is/was valid for use.",
        # if property is element of this resource.
        element_property=True,
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="The namespace for the identifier value",
        description=(
            "Establishes the namespace for the value - that is, a URL that "
            "describes a set values that are unique."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Description of identifier",
        description=(
            "A coded type for the identifier that can be used to determine which "
            "identifier to use for a specific purpose. See "
            "http://hl7.org/fhir/ValueSet/identifier-type"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_strength="extensible",
        binding_uri="http://hl7.org/fhir/ValueSet/identifier-type",
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="usual | official | temp | secondary | old (If known)",
        description=(
            "The purpose of this identifier. See "
            "http://hl7.org/fhir/ValueSet/identifier-use"
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["usual", "official", "temp", "secondary", "old"],
        # valueset binding
        binding_strength="required",
        binding_uri="http://hl7.org/fhir/ValueSet/identifier-use",
        binding_version="4.3.0",
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_use", title="Extension field for ``use``."
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="The value that is unique",
        description=(
            "The portion of the identifier typically relevant to the user and which"
            " is unique within the context of the system."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Identifier`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "use",
            "type",
            "system",
            "value",
            "period",
            "assigner",
        ]
