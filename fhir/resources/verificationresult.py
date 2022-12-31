# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/VerificationResult
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class VerificationResult(domainresource.DomainResource):
    """
    Describes validation requirements, source(s), status and dates for one or
    more elements.
    """

    resource_type = Field("VerificationResult", const=True)

    attestation: fhirtypes.VerificationResultAttestationType = Field(
        None,
        alias="attestation",
        title="Information about the entity attesting to information",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    failureAction: fhirtypes.CodeableConceptType = Field(
        None,
        alias="failureAction",
        title="fatal | warn | rec-only | none",
        description=(
            "The result if validation fails (fatal; warning; record only; none). "
            "See http://hl7.org/fhir/ValueSet/verificationresult-failure-action"
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["fatal", "warn", "rec-only", "none"],
        # valueset binding
        binding_description="The result if validation fails.",
        binding_strength="preferred",
        binding_uri="http://hl7.org/fhir/ValueSet/verificationresult-failure-action",
    )

    frequency: fhirtypes.TimingType = Field(
        None,
        alias="frequency",
        title="Frequency of revalidation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    lastPerformed: fhirtypes.DateTime = Field(
        None,
        alias="lastPerformed",
        title=(
            "The date/time validation was last completed (including failed "
            "validations)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    lastPerformed__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastPerformed", title="Extension field for ``lastPerformed``."
    )

    need: fhirtypes.CodeableConceptType = Field(
        None,
        alias="need",
        title="none | initial | periodic",
        description=(
            "The frequency with which the target must be validated (none; initial; "
            "periodic). See http://hl7.org/fhir/ValueSet/verificationresult-need"
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["none", "initial", "periodic"],
        # valueset binding
        binding_description="The frequency with which the target must be validated.",
        binding_strength="preferred",
        binding_uri="http://hl7.org/fhir/ValueSet/verificationresult-need",
    )

    nextScheduled: fhirtypes.Date = Field(
        None,
        alias="nextScheduled",
        title="The date when target is next validated, if appropriate",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    nextScheduled__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_nextScheduled", title="Extension field for ``nextScheduled``."
    )

    primarySource: typing.List[fhirtypes.VerificationResultPrimarySourceType] = Field(
        None,
        alias="primarySource",
        title="Information about the primary source(s) involved in validation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "attested | validated | in-process | req-revalid | val-fail | reval-" "fail"
        ),
        description=(
            "The validation status of the target (attested; validated; in process; "
            "requires revalidation; validation failed; revalidation failed). See "
            "http://hl7.org/fhir/ValueSet/verificationresult-status"
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "attested",
            "validated",
            "in-process",
            "req-revalid",
            "val-fail",
            "reval-fail",
        ],
        # valueset binding
        binding_description="The validation status of the target.",
        binding_strength="required",
        binding_uri="http://hl7.org/fhir/ValueSet/verificationresult-status",
        binding_version="4.3.0",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusDate: fhirtypes.DateTime = Field(
        None,
        alias="statusDate",
        title="When the validation status was updated",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_statusDate", title="Extension field for ``statusDate``."
    )

    target: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="target",
        title="A resource that was validated",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    targetLocation: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="targetLocation",
        title="The fhirpath location(s) within the resource that was validated",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    targetLocation__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_targetLocation", title="Extension field for ``targetLocation``."
    )

    validationProcess: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="validationProcess",
        title=(
            "The primary process by which the target is validated (edit check; "
            "value set; primary source; multiple sources; standalone; in context)"
        ),
        description="See http://hl7.org/fhir/ValueSet/verificationresult-validation-process",
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="The primary process by which the target is validated.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/verificationresult-validation-process",
    )

    validationType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="validationType",
        title="nothing | primary | multiple",
        description=(
            "What the target is validated against (nothing; primary source; "
            "multiple sources). See "
            "http://hl7.org/fhir/ValueSet/verificationresult-validation-type"
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["nothing", "primary", "multiple"],
        # valueset binding
        binding_description="What the target is validated against.",
        binding_strength="preferred",
        binding_uri="http://hl7.org/fhir/ValueSet/verificationresult-validation-type",
    )

    validator: typing.List[fhirtypes.VerificationResultValidatorType] = Field(
        None,
        alias="validator",
        title="Information about the entity validating information",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``VerificationResult`` according specification,
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
            "target",
            "targetLocation",
            "need",
            "status",
            "statusDate",
            "validationType",
            "validationProcess",
            "frequency",
            "lastPerformed",
            "nextScheduled",
            "failureAction",
            "primarySource",
            "attestation",
            "validator",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2092(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class VerificationResultAttestation(backboneelement.BackboneElement):
    """
    Information about the entity attesting to information.
    """

    resource_type = Field("VerificationResultAttestation", const=True)

    communicationMethod: fhirtypes.CodeableConceptType = Field(
        None,
        alias="communicationMethod",
        title="The method by which attested information was submitted/retrieved",
        description=(
            "The method by which attested information was submitted/retrieved "
            "(manual; API; Push). See "
            "http://hl7.org/fhir/ValueSet/verificationresult-communication-method"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Method for communicating with the data source (manual; API; Push).",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/verificationresult-communication-method",
    )

    date: fhirtypes.Date = Field(
        None,
        alias="date",
        title="The date the information was attested to",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title=(
            "When the who is asserting on behalf of another (organization or "
            "individual)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization", "Practitioner", "PractitionerRole"],
    )

    proxyIdentityCertificate: fhirtypes.String = Field(
        None,
        alias="proxyIdentityCertificate",
        title=(
            "A digital identity certificate associated with the proxy entity "
            "submitting attested information on behalf of the attestation source"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    proxyIdentityCertificate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_proxyIdentityCertificate",
        title="Extension field for ``proxyIdentityCertificate``.",
    )

    proxySignature: fhirtypes.SignatureType = Field(
        None,
        alias="proxySignature",
        title="Proxy signature",
        description=(
            "Signed assertion by the proxy entity indicating that they have the "
            "right to submit attested information on behalf of the attestation "
            "source."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sourceIdentityCertificate: fhirtypes.String = Field(
        None,
        alias="sourceIdentityCertificate",
        title="A digital identity certificate associated with the attestation source",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    sourceIdentityCertificate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_sourceIdentityCertificate",
        title="Extension field for ``sourceIdentityCertificate``.",
    )

    sourceSignature: fhirtypes.SignatureType = Field(
        None,
        alias="sourceSignature",
        title="Attester signature",
        description=(
            "Signed assertion by the attestation source that they have attested to "
            "the information."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    who: fhirtypes.ReferenceType = Field(
        None,
        alias="who",
        title="The individual or organization attesting to information",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole", "Organization"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``VerificationResultAttestation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "who",
            "onBehalfOf",
            "communicationMethod",
            "date",
            "sourceIdentityCertificate",
            "proxyIdentityCertificate",
            "proxySignature",
            "sourceSignature",
        ]


class VerificationResultPrimarySource(backboneelement.BackboneElement):
    """
    Information about the primary source(s) involved in validation.
    """

    resource_type = Field("VerificationResultPrimarySource", const=True)

    canPushUpdates: fhirtypes.CodeableConceptType = Field(
        None,
        alias="canPushUpdates",
        title="yes | no | undetermined",
        description=(
            "Ability of the primary source to push updates/alerts (yes; no; "
            "undetermined). See http://hl7.org/fhir/ValueSet/verificationresult-"
            "can-push-updates"
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["yes", "no", "undetermined"],
        # valueset binding
        binding_description="Ability of the primary source to push updates/alerts.",
        binding_strength="preferred",
        binding_uri="http://hl7.org/fhir/ValueSet/verificationresult-can-push-updates",
    )

    communicationMethod: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="communicationMethod",
        title="Method for exchanging information with the primary source",
        description=(
            "Method for communicating with the primary source (manual; API; Push). "
            "See http://hl7.org/fhir/ValueSet/verificationresult-communication-"
            "method"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Method for communicating with the data source (manual; API; Push).",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/verificationresult-communication-method",
    )

    pushTypeAvailable: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="pushTypeAvailable",
        title="specific | any | source",
        description=(
            "Type of alerts/updates the primary source can send (specific requested"
            " changes; any changes; as defined by source). See "
            "http://hl7.org/fhir/ValueSet/verificationresult-push-type-available"
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["specific", "any", "source"],
        # valueset binding
        binding_description="Type of alerts/updates the primary source can send.",
        binding_strength="preferred",
        binding_uri="http://hl7.org/fhir/ValueSet/verificationresult-push-type-available",
    )

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title=(
            "Type of primary source (License Board; Primary Education; Continuing "
            "Education; Postal Service; Relationship owner; Registration Authority;"
            " legal source; issuing source; authoritative source)"
        ),
        description=(
            "See http://hl7.org/fhir/ValueSet/verificationresult-primary-source-" "type"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Type of the validation primary source.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/verificationresult-primary-source-type",
    )

    validationDate: fhirtypes.DateTime = Field(
        None,
        alias="validationDate",
        title="When the target was validated against the primary source",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    validationDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_validationDate", title="Extension field for ``validationDate``."
    )

    validationStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="validationStatus",
        title="successful | failed | unknown",
        description=(
            "Status of the validation of the target against the primary source "
            "(successful; failed; unknown). See "
            "http://hl7.org/fhir/ValueSet/verificationresult-validation-status"
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["successful", "failed", "unknown"],
        # valueset binding
        binding_description="Status of the validation of the target against the primary source.",
        binding_strength="preferred",
        binding_uri="http://hl7.org/fhir/ValueSet/verificationresult-validation-status",
    )

    who: fhirtypes.ReferenceType = Field(
        None,
        alias="who",
        title="Reference to the primary source",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization", "Practitioner", "PractitionerRole"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``VerificationResultPrimarySource`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "who",
            "type",
            "communicationMethod",
            "validationStatus",
            "validationDate",
            "canPushUpdates",
            "pushTypeAvailable",
        ]


class VerificationResultValidator(backboneelement.BackboneElement):
    """
    Information about the entity validating information.
    """

    resource_type = Field("VerificationResultValidator", const=True)

    attestationSignature: fhirtypes.SignatureType = Field(
        None,
        alias="attestationSignature",
        title="Validator signature",
        description=(
            "Signed assertion by the validator that they have validated the "
            "information."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identityCertificate: fhirtypes.String = Field(
        None,
        alias="identityCertificate",
        title="A digital identity certificate associated with the validator",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    identityCertificate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_identityCertificate",
        title="Extension field for ``identityCertificate``.",
    )

    organization: fhirtypes.ReferenceType = Field(
        ...,
        alias="organization",
        title="Reference to the organization validating information",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``VerificationResultValidator`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "organization",
            "identityCertificate",
            "attestationSignature",
        ]
