# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EnrollmentResponse
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class EnrollmentResponse(domainresource.DomainResource):
    """
    EnrollmentResponse resource.
    This resource provides enrollment and plan details from the processing of
    an EnrollmentRequest resource.
    """

    resource_type = Field("EnrollmentResponse", const=True)

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Creation date",
        description=(
            "The date when the enclosed suite of services were performed or "
            "completed."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Disposition Message",
        description="A description of the status of the adjudication.",
        # if property is element of this resource.
        element_property=True,
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier",
        description="The Response business identifier.",
        # if property is element of this resource.
        element_property=True,
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Insurer",
        description="The Insurer who produced this adjudicated response.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    outcome: fhirtypes.Code = Field(
        None,
        alias="outcome",
        title="queued | complete | error | partial",
        description=(
            "Processing status: error, complete. See "
            "http://hl7.org/fhir/ValueSet/remittance-outcome"
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["queued", "complete", "error", "partial"],
        # valueset binding
        binding_description="The outcome of the processing.",
        binding_strength="required",
        binding_uri="http://hl7.org/fhir/ValueSet/remittance-outcome",
        binding_version="4.3.0",
    )
    outcome__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_outcome", title="Extension field for ``outcome``."
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Claim reference",
        description="Original request resource reference.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EnrollmentRequest"],
    )

    requestProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="requestProvider",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the services rendered to the "
            "patient."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole", "Organization"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description=(
            "The status of the resource instance. See "
            "http://hl7.org/fhir/ValueSet/fm-status"
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "cancelled", "draft", "entered-in-error"],
        # valueset binding
        binding_description="A code specifying the state of the resource instance.",
        binding_strength="required",
        binding_uri="http://hl7.org/fhir/ValueSet/fm-status",
        binding_version="4.3.0",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EnrollmentResponse`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "status",
            "request",
            "outcome",
            "disposition",
            "created",
            "organization",
            "requestProvider",
        ]
