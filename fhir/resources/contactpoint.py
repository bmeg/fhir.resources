# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ContactPoint
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic import Field

from . import element, fhirtypes


class ContactPoint(element.Element):
    """
    Details of a Technology mediated contact point (phone, fax, email, etc.).
    Details for all kinds of technology mediated contact points for a person or
    organization, including telephone, email, etc.
    """

    resource_type = Field("ContactPoint", const=True)

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Time period when the contact point was/is in use",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    rank: fhirtypes.PositiveInt = Field(
        None,
        alias="rank",
        title="Specify preferred order of use (1 = highest)",
        description=(
            "Specifies a preferred order in which to use a set of contacts. "
            "ContactPoints with lower rank values are more preferred than those "
            "with higher rank values."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    rank__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rank", title="Extension field for ``rank``."
    )

    system: fhirtypes.Code = Field(
        None,
        alias="system",
        title="phone | fax | email | pager | url | sms | other",
        description=(
            "Telecommunications form for contact point - what communications system"
            " is required to make use of the contact. See "
            "http://hl7.org/fhir/ValueSet/contact-point-system"
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["phone", "fax", "email", "pager", "url", "sms", "other"],
        # valueset binding
        binding_strength="required",
        binding_uri="http://hl7.org/fhir/ValueSet/contact-point-system",
        binding_version="4.3.0",
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="home | work | temp | old | mobile - purpose of this contact point",
        description=(
            "Identifies the purpose for the contact point. See "
            "http://hl7.org/fhir/ValueSet/contact-point-use"
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["home", "work", "temp", "old", "mobile"],
        # valueset binding
        binding_strength="required",
        binding_uri="http://hl7.org/fhir/ValueSet/contact-point-use",
        binding_version="4.3.0",
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_use", title="Extension field for ``use``."
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="The actual contact point details",
        description=(
            "The actual contact point details, in a form that is meaningful to the "
            "designated communication system (i.e. phone number or email address)."
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
        ``ContactPoint`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "system", "value", "use", "rank", "period"]
