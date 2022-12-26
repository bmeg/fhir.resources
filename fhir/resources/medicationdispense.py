# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationDispense
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


class MedicationDispense(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Dispensing a medication to a named patient.
    Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """

    resource_type = Field("MedicationDispense", const=True)

    authorizingPrescription: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="authorizingPrescription",
        title="Medication order that authorizes the dispense",
        description="Indicates the medication order that is being dispensed against.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicationRequest"],
        backref="medication_dispense_authorizingPrescription",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of medication dispense",
        description=(
            "Indicates the type of medication dispense (for example, where the "
            "medication is expected to be consumed or administered (i.e. inpatient "
            "or outpatient)). See http://hl7.org/fhir/ValueSet/medicationdispense-"
            "category"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="A code describing where the dispensed medication is expected to be consumed or administered.",
        binding_strength="preferred",
        binding_uri="http://hl7.org/fhir/ValueSet/medicationdispense-category",
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Encounter / Episode associated with event",
        description=(
            "The encounter or episode of care that establishes the context for this"
            " event."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter", "EpisodeOfCare"],
        backref="medication_dispense_context",
    )

    daysSupply: fhirtypes.QuantityType = Field(
        None,
        alias="daysSupply",
        title="Amount of medication expressed as a timing amount",
        description="The amount of medication expressed as a timing amount.",
        # if property is element of this resource.
        element_property=True,
    )

    destination: fhirtypes.ReferenceType = Field(
        None,
        alias="destination",
        title="Where the medication was sent",
        description=(
            "Identification of the facility/location where the medication was "
            "shipped to, as part of the dispense event."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
        backref="medication_dispense_destination",
    )

    detectedIssue: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="detectedIssue",
        title="Clinical issue with action",
        description=(
            "Indicates an actual or potential clinical issue with or between one or"
            " more active or proposed clinical actions for a patient; e.g. drug-"
            "drug interaction, duplicate therapy, dosage alert etc."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DetectedIssue"],
        backref="medication_dispense_detectedIssue",
    )

    dosageInstruction: typing.List[fhirtypes.DosageType] = Field(
        None,
        alias="dosageInstruction",
        title=(
            "How the medication is to be used by the patient or administered by the"
            " caregiver"
        ),
        description="Indicates how the medication is to be used by the patient.",
        # if property is element of this resource.
        element_property=True,
    )

    eventHistory: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="eventHistory",
        title="A list of relevant lifecycle events",
        description=(
            "A summary of the events of interest that have occurred, such as when "
            "the dispense was verified."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Provenance"],
        backref="medication_dispense_eventHistory",
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External identifier",
        description=(
            "Identifiers associated with this Medication Dispense that are defined "
            "by business processes and/or used to refer to it when a direct URL "
            "reference to the resource itself is not appropriate. They are business"
            " identifiers assigned to this resource by the performer or other "
            "systems and remain constant as the resource is updated and propagates "
            "from server to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Where the dispense occurred",
        description="The principal physical location where the dispense was performed.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
        backref="medication_dispense_location",
    )

    medicationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="medicationCodeableConcept",
        title="What medication was supplied",
        description=(
            "Identifies the medication being administered. This is either a link to"
            " a resource representing the details of the medication or a simple "
            "attribute carrying a code that identifies the medication from a known "
            "list of medications. See http://hl7.org/fhir/ValueSet/medication-codes"
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e medication[x]
        one_of_many="medication",
        one_of_many_required=True,
        # valueset binding
        binding_description="A coded concept identifying which substance or product can be dispensed.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/medication-codes",
    )

    medicationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="medicationReference",
        title="What medication was supplied",
        description=(
            "Identifies the medication being administered. This is either a link to"
            " a resource representing the details of the medication or a simple "
            "attribute carrying a code that identifies the medication from a known "
            "list of medications. See http://hl7.org/fhir/ValueSet/medication-codes"
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e medication[x]
        one_of_many="medication",
        one_of_many_required=True,
        # valueset binding
        binding_description="A coded concept identifying which substance or product can be dispensed.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/medication-codes",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Medication"],
        backref="medication_dispense_medicationReference",
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Information about the dispense",
        description=(
            "Extra information about the dispense that could not be conveyed in the"
            " other attributes."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    partOf: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Event that dispense is part of",
        description="The procedure that trigger the dispense.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Procedure"],
        backref="medication_dispense_partOf",
    )

    performer: typing.List[fhirtypes.MedicationDispensePerformerType] = Field(
        None,
        alias="performer",
        title="Who performed event",
        description="Indicates who or what performed the event.",
        # if property is element of this resource.
        element_property=True,
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Amount dispensed",
        description=(
            "The amount of medication that has been dispensed. Includes unit of "
            "measure."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    receiver: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="receiver",
        title="Who collected the medication",
        description=(
            "Identifies the person who picked up the medication.  This will usually"
            " be a patient or their caregiver, but some cases exist where it can be"
            " a healthcare professional."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Practitioner"],
        backref="medication_dispense_receiver",
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "preparation | in-progress | cancelled | on-hold | completed | entered-"
            "in-error | stopped | declined | unknown"
        ),
        description=(
            "A code specifying the state of the set of dispense events. See "
            "http://hl7.org/fhir/ValueSet/medicationdispense-status"
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "preparation",
            "in-progress",
            "cancelled",
            "on-hold",
            "completed",
            "entered-in-error",
            "stopped",
            "declined",
            "unknown",
        ],
        # valueset binding
        binding_description="Describes the lifecycle of the dispense.",
        binding_strength="required",
        binding_uri="http://hl7.org/fhir/ValueSet/medicationdispense-status",
        binding_version="4.3.0",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReasonCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="statusReasonCodeableConcept",
        title="Why a dispense was not performed",
        description=(
            "Indicates the reason why a dispense was not performed. See "
            "http://hl7.org/fhir/ValueSet/medicationdispense-status-reason"
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e statusReason[x]
        one_of_many="statusReason",
        one_of_many_required=False,
        # valueset binding
        binding_description="A code describing why a dispense was not performed.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/medicationdispense-status-reason",
    )

    statusReasonReference: fhirtypes.ReferenceType = Field(
        None,
        alias="statusReasonReference",
        title="Why a dispense was not performed",
        description=(
            "Indicates the reason why a dispense was not performed. See "
            "http://hl7.org/fhir/ValueSet/medicationdispense-status-reason"
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e statusReason[x]
        one_of_many="statusReason",
        one_of_many_required=False,
        # valueset binding
        binding_description="A code describing why a dispense was not performed.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/medicationdispense-status-reason",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DetectedIssue"],
        backref="medication_dispense_statusReasonReference",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Who the dispense is for",
        description=(
            "A link to a resource representing the person or the group to whom the "
            "medication will be given."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
        backref="medication_dispense_subject",
    )

    substitution: fhirtypes.MedicationDispenseSubstitutionType = Field(
        None,
        alias="substitution",
        title="Whether a substitution was performed on the dispense",
        description=(
            "Indicates whether or not substitution was made as part of the "
            "dispense.  In some cases, substitution will be expected but does not "
            "happen, in other cases substitution is not expected but does happen.  "
            "This block explains what substitution did or did not happen and why.  "
            "If nothing is specified, substitution was not done."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    supportingInformation: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInformation",
        title="Information that supports the dispensing of the medication",
        description="Additional information that supports the medication being dispensed.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
        backref="medication_dispense_supportingInformation",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Trial fill, partial fill, emergency fill, etc.",
        description=(
            "Indicates the type of dispensing event that is performed. For example,"
            " Trial Fill, Completion of Trial, Partial Fill, Emergency Fill, "
            "Samples, etc. See "
            "http://terminology.hl7.org/ValueSet/v3-ActPharmacySupplyType"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="ActPharmacySupplyType",
        binding_strength="example",
        binding_uri="http://terminology.hl7.org/ValueSet/v3-ActPharmacySupplyType",
    )

    whenHandedOver: fhirtypes.DateTime = Field(
        None,
        alias="whenHandedOver",
        title="When product was given out",
        description=(
            "The time the dispensed product was provided to the patient or their "
            "representative."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    whenHandedOver__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_whenHandedOver", title="Extension field for ``whenHandedOver``."
    )

    whenPrepared: fhirtypes.DateTime = Field(
        None,
        alias="whenPrepared",
        title="When product was packaged and reviewed",
        description="The time when the dispensed product was packaged and reviewed.",
        # if property is element of this resource.
        element_property=True,
    )
    whenPrepared__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_whenPrepared", title="Extension field for ``whenPrepared``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationDispense`` according specification,
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
            "partOf",
            "status",
            "statusReasonCodeableConcept",
            "statusReasonReference",
            "category",
            "medicationCodeableConcept",
            "medicationReference",
            "subject",
            "context",
            "supportingInformation",
            "performer",
            "location",
            "authorizingPrescription",
            "type",
            "quantity",
            "daysSupply",
            "whenPrepared",
            "whenHandedOver",
            "destination",
            "receiver",
            "note",
            "dosageInstruction",
            "substitution",
            "detectedIssue",
            "eventHistory",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2026(
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

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_2026(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "medication": ["medicationCodeableConcept", "medicationReference"],
            "statusReason": ["statusReasonCodeableConcept", "statusReasonReference"],
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values


class MedicationDispensePerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who performed event.
    Indicates who or what performed the event.
    """

    resource_type = Field("MedicationDispensePerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Individual who was performing",
        description=(
            "The device, practitioner, etc. who performed the action.  It should be"
            " assumed that the actor is the dispenser of the medication."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "Patient",
            "Device",
            "RelatedPerson",
        ],
        backref="medication_dispense.performer_actor",
    )

    function: fhirtypes.CodeableConceptType = Field(
        None,
        alias="function",
        title="Who performed the dispense and what they did",
        description=(
            "Distinguishes the type of performer in the dispense.  For example, "
            "date enterer, packager, final checker. See "
            "http://hl7.org/fhir/ValueSet/medicationdispense-performer-function"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="A code describing the role an individual played in dispensing a medication.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/medicationdispense-performer-function",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationDispensePerformer`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "function", "actor"]


class MedicationDispenseSubstitution(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Whether a substitution was performed on the dispense.
    Indicates whether or not substitution was made as part of the dispense.  In
    some cases, substitution will be expected but does not happen, in other
    cases substitution is not expected but does happen.  This block explains
    what substitution did or did not happen and why.  If nothing is specified,
    substitution was not done.
    """

    resource_type = Field("MedicationDispenseSubstitution", const=True)

    reason: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="Why was substitution made",
        description=(
            "Indicates the reason for the substitution (or lack of substitution) "
            "from what was prescribed. See http://terminology.hl7.org/ValueSet/v3-S"
            "ubstanceAdminSubstitutionReason"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="SubstanceAdminSubstitutionReason",
        binding_strength="example",
        binding_uri="http://terminology.hl7.org/ValueSet/v3-SubstanceAdminSubstitutionReason",
    )

    responsibleParty: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="responsibleParty",
        title="Who is responsible for the substitution",
        description=(
            "The person or organization that has primary responsibility for the "
            "substitution."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole"],
        backref="medication_dispense.substitution_responsibleParty",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "Code signifying whether a different drug was dispensed from what was "
            "prescribed"
        ),
        description=(
            "A code signifying whether a different drug was dispensed from what was"
            " prescribed. See http://terminology.hl7.org/ValueSet/v3-ActSubstanceAd"
            "minSubstitutionCode"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="ActSubstanceAdminSubstitutionCode",
        binding_strength="example",
        binding_uri="http://terminology.hl7.org/ValueSet/v3-ActSubstanceAdminSubstitutionCode",
    )

    wasSubstituted: bool = Field(
        None,
        alias="wasSubstituted",
        title="Whether a substitution was or was not performed on the dispense",
        description=(
            "True if the dispenser dispensed a different drug or product from what "
            "was prescribed."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    wasSubstituted__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_wasSubstituted", title="Extension field for ``wasSubstituted``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicationDispenseSubstitution`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "wasSubstituted",
            "type",
            "reason",
            "responsibleParty",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3344(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("wasSubstituted", "wasSubstituted__ext")]
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
