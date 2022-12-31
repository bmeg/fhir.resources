# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Address
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import element, fhirtypes


class Address(element.Element):
    """
    An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).
    An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).  This data type may be used to convey
    addresses for use in delivering mail as well as for visiting locations
    which might not be valid for mail delivery.  There are a variety of postal
    address formats defined around the world.
    """

    resource_type = Field("Address", const=True)

    city: fhirtypes.String = Field(
        None,
        alias="city",
        title="Name of city, town etc.",
        description=(
            "The name of the city, town, suburb, village or other community or "
            "delivery center."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    city__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_city", title="Extension field for ``city``."
    )

    country: fhirtypes.String = Field(
        None,
        alias="country",
        title="Country (e.g. can be ISO 3166 2 or 3 letter code)",
        description="Country - a nation as commonly understood or generally accepted.",
        # if property is element of this resource.
        element_property=True,
    )
    country__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_country", title="Extension field for ``country``."
    )

    district: fhirtypes.String = Field(
        None,
        alias="district",
        title="District name (aka county)",
        description="The name of the administrative area (county).",
        # if property is element of this resource.
        element_property=True,
    )
    district__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_district", title="Extension field for ``district``."
    )

    line: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="line",
        title="Street name, number, direction & P.O. Box etc.",
        description=(
            "This component contains the house number, apartment number, street "
            "name, street direction,  P.O. Box number, delivery hints, and similar "
            "address information."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    line__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_line", title="Extension field for ``line``.")

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Time period when address was/is in use",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    postalCode: fhirtypes.String = Field(
        None,
        alias="postalCode",
        title="Postal code for area",
        description="A postal code designating a region defined by the postal service.",
        # if property is element of this resource.
        element_property=True,
    )
    postalCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_postalCode", title="Extension field for ``postalCode``."
    )

    state: fhirtypes.String = Field(
        None,
        alias="state",
        title="Sub-unit of country (abbreviations ok)",
        description=(
            "Sub-unit of a country with limited sovereignty in a federally "
            "organized country. A code may be used if codes are in common use (e.g."
            " US 2 letter state codes)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    state__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_state", title="Extension field for ``state``."
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Text representation of the address",
        description=(
            "Specifies the entire address as it should be displayed e.g. on a "
            "postal label. This may be provided instead of or as well as the "
            "specific parts."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="postal | physical | both",
        description=(
            "Distinguishes between physical addresses (those you can visit) and "
            "mailing addresses (e.g. PO Boxes and care-of addresses). Most "
            "addresses are both. See http://hl7.org/fhir/ValueSet/address-type"
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["postal", "physical", "both"],
        # valueset binding
        binding_description="The type of an address (physical / postal).",
        binding_strength="required",
        binding_uri="http://hl7.org/fhir/ValueSet/address-type",
        binding_version="4.3.0",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="home | work | temp | old | billing - purpose of this address",
        description=(
            "The purpose of this address. See http://hl7.org/fhir/ValueSet/address-"
            "use"
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["home", "work", "temp", "old", "billing"],
        # valueset binding
        binding_description="The use of an address (home / work / etc.).",
        binding_strength="required",
        binding_uri="http://hl7.org/fhir/ValueSet/address-use",
        binding_version="4.3.0",
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_use", title="Extension field for ``use``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Address`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "use",
            "type",
            "text",
            "line",
            "city",
            "district",
            "state",
            "postalCode",
            "country",
            "period",
        ]
