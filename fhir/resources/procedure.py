# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Procedure
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


class Procedure(domainresource.DomainResource):
    """
    An action that is being or was performed on a patient.
    An action that is or was performed on or for a patient. This can be a
    physical intervention like an operation, or less invasive like long term
    services, counseling, or hypnotherapy.
    """

    resource_type = Field("Procedure", const=True)

    asserter: fhirtypes.ReferenceType = Field(
        None,
        alias="asserter",
        title="Person who asserts this procedure",
        description="Individual who is making the procedure statement.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "RelatedPerson",
            "Practitioner",
            "PractitionerRole",
        ],
    )

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="A request for this procedure",
        description=(
            "A reference to a resource that contains details of the request for "
            "this procedure."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CarePlan", "ServiceRequest"],
    )

    bodySite: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="bodySite",
        title="Target body sites",
        description=(
            "Detailed and structured anatomical location information. Multiple "
            "locations are allowed - e.g. multiple punch biopsies of a lesion. See "
            "http://hl7.org/fhir/ValueSet/body-site"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="SNOMED CT Body site concepts",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/body-site",
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Classification of the procedure",
        description=(
            "A code that classifies the procedure for searching, sorting and "
            'display purposes (e.g. "Surgical Procedure"). See '
            "http://hl7.org/fhir/ValueSet/procedure-category"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="A code that classifies a procedure for searching, sorting and display purposes.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/procedure-category",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Identification of the procedure",
        description=(
            "The specific procedure that is performed. Use text if the exact nature"
            ' of the procedure cannot be coded (e.g. "Laparoscopic Appendectomy"). '
            "See http://hl7.org/fhir/ValueSet/procedure-code"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="A code to identify a specific procedure .",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/procedure-code",
    )

    complication: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="complication",
        title="Complication following the procedure",
        description=(
            "Any complications that occurred during the procedure, or in the "
            "immediate post-performance period. These are generally tracked "
            "separately from the notes, which will typically describe the procedure"
            " itself rather than any 'post procedure' issues. See "
            "http://hl7.org/fhir/ValueSet/condition-code"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Codes describing complications that resulted from a procedure.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/condition-code",
    )

    complicationDetail: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="complicationDetail",
        title="A condition that is a result of the procedure",
        description=(
            "Any complications that occurred during the procedure, or in the "
            "immediate post-performance period."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition"],
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter created as part of",
        description=(
            "The Encounter during which this Procedure was created or performed or "
            "to which the creation of this record is tightly associated."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    focalDevice: typing.List[fhirtypes.ProcedureFocalDeviceType] = Field(
        None,
        alias="focalDevice",
        title="Manipulated, implanted, or removed device",
        description=(
            "A device that is implanted, removed or otherwise manipulated "
            "(calibration, battery replacement, fitting a prosthesis, attaching a "
            "wound-vac, etc.) as a focal portion of the Procedure."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    followUp: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="followUp",
        title="Instructions for follow up",
        description=(
            "If the procedure required specific follow up - e.g. removal of "
            "sutures. The follow up may be represented as a simple note or could "
            "potentially be more complex, in which case the CarePlan resource can "
            "be used. See http://hl7.org/fhir/ValueSet/procedure-followup"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Specific follow up required for a procedure e.g. removal of sutures.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/procedure-followup",
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External Identifiers for this procedure",
        description=(
            "Business identifiers assigned to this procedure by the performer or "
            "other systems which remain constant as the resource is updated and is "
            "propagated from server to server."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    instantiatesCanonical: typing.List[typing.Optional[fhirtypes.Canonical]] = Field(
        None,
        alias="instantiatesCanonical",
        title="Instantiates FHIR protocol or definition",
        description=(
            "The URL pointing to a FHIR-defined protocol, guideline, order set or "
            "other definition that is adhered to in whole or in part by this "
            "Procedure."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "PlanDefinition",
            "ActivityDefinition",
            "Measure",
            "OperationDefinition",
            "Questionnaire",
        ],
    )
    instantiatesCanonical__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``.",
    )

    instantiatesUri: typing.List[typing.Optional[fhirtypes.Uri]] = Field(
        None,
        alias="instantiatesUri",
        title="Instantiates external protocol or definition",
        description=(
            "The URL pointing to an externally maintained protocol, guideline, "
            "order set or other definition that is adhered to in whole or in part "
            "by this Procedure."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    instantiatesUri__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_instantiatesUri", title="Extension field for ``instantiatesUri``."
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Where the procedure happened",
        description=(
            "The location where the procedure actually happened.  E.g. a newborn at"
            " home, a tracheostomy at a restaurant."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Additional information about the procedure",
        description="Any other notes and comments about the procedure.",
        # if property is element of this resource.
        element_property=True,
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="The result of procedure",
        description=(
            "The outcome of the procedure - did it resolve the reasons for the "
            "procedure being performed? See http://hl7.org/fhir/ValueSet/procedure-"
            "outcome"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="An outcome of a procedure - whether it was resolved or otherwise.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/procedure-outcome",
    )

    partOf: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Part of referenced event",
        description=(
            "A larger event of which this particular procedure is a component or "
            "step."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Procedure", "Observation", "MedicationAdministration"],
    )

    performedAge: fhirtypes.AgeType = Field(
        None,
        alias="performedAge",
        title="When the procedure was performed",
        description=(
            "Estimated or actual date, date-time, period, or age when the procedure"
            " was performed.  Allows a period to support complex procedures that "
            "span more than one date, and also allows for the length of the "
            "procedure to be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e performed[x]
        one_of_many="performed",
        one_of_many_required=False,
    )

    performedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="performedDateTime",
        title="When the procedure was performed",
        description=(
            "Estimated or actual date, date-time, period, or age when the procedure"
            " was performed.  Allows a period to support complex procedures that "
            "span more than one date, and also allows for the length of the "
            "procedure to be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e performed[x]
        one_of_many="performed",
        one_of_many_required=False,
    )
    performedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_performedDateTime",
        title="Extension field for ``performedDateTime``.",
    )

    performedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="performedPeriod",
        title="When the procedure was performed",
        description=(
            "Estimated or actual date, date-time, period, or age when the procedure"
            " was performed.  Allows a period to support complex procedures that "
            "span more than one date, and also allows for the length of the "
            "procedure to be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e performed[x]
        one_of_many="performed",
        one_of_many_required=False,
    )

    performedRange: fhirtypes.RangeType = Field(
        None,
        alias="performedRange",
        title="When the procedure was performed",
        description=(
            "Estimated or actual date, date-time, period, or age when the procedure"
            " was performed.  Allows a period to support complex procedures that "
            "span more than one date, and also allows for the length of the "
            "procedure to be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e performed[x]
        one_of_many="performed",
        one_of_many_required=False,
    )

    performedString: fhirtypes.String = Field(
        None,
        alias="performedString",
        title="When the procedure was performed",
        description=(
            "Estimated or actual date, date-time, period, or age when the procedure"
            " was performed.  Allows a period to support complex procedures that "
            "span more than one date, and also allows for the length of the "
            "procedure to be captured."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e performed[x]
        one_of_many="performed",
        one_of_many_required=False,
    )
    performedString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_performedString", title="Extension field for ``performedString``."
    )

    performer: typing.List[fhirtypes.ProcedurePerformerType] = Field(
        None,
        alias="performer",
        title="The people who performed the procedure",
        description='Limited to "real" people rather than equipment.',
        # if property is element of this resource.
        element_property=True,
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Coded reason procedure performed",
        description=(
            "The coded reason why the procedure was performed. This may be a coded "
            "entity of some type, or may simply be present as text. See "
            "http://hl7.org/fhir/ValueSet/procedure-reason"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="A code that identifies the reason a procedure is  required.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/procedure-reason",
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="The justification that the procedure was performed",
        description="The justification of why the procedure was performed.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Observation",
            "Procedure",
            "DiagnosticReport",
            "DocumentReference",
        ],
    )

    recorder: fhirtypes.ReferenceType = Field(
        None,
        alias="recorder",
        title="Who recorded the procedure",
        description=(
            "Individual who recorded the record and takes responsibility for its "
            "content."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "RelatedPerson",
            "Practitioner",
            "PractitionerRole",
        ],
    )

    report: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="report",
        title="Any report resulting from the procedure",
        description=(
            "This could be a histology result, pathology report, surgical report, "
            "etc."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DiagnosticReport", "DocumentReference", "Composition"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "preparation | in-progress | not-done | on-hold | stopped | completed |"
            " entered-in-error | unknown"
        ),
        description=(
            "A code specifying the state of the procedure. Generally, this will be "
            "the in-progress or completed state. See "
            "http://hl7.org/fhir/ValueSet/event-status"
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "preparation",
            "in-progress",
            "not-done",
            "on-hold",
            "stopped",
            "completed",
            "entered-in-error",
            "unknown",
        ],
        # valueset binding
        binding_description="A code specifying the state of the procedure.",
        binding_strength="required",
        binding_uri="http://hl7.org/fhir/ValueSet/event-status",
        binding_version="4.3.0",
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="statusReason",
        title="Reason for current status",
        description=(
            "Captures the reason for the current state of the procedure. See "
            "http://hl7.org/fhir/ValueSet/procedure-not-performed-reason"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="A code that identifies the reason a procedure was not performed.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/procedure-not-performed-reason",
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who the procedure was performed on",
        description="The person, animal or group on which the procedure was performed.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    usedCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="usedCode",
        title="Coded items used during the procedure",
        description=(
            "Identifies coded items that were used as part of the procedure. See "
            "http://hl7.org/fhir/ValueSet/device-kind"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Codes describing items used during a procedure.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/device-kind",
    )

    usedReference: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="usedReference",
        title="Items used during procedure",
        description=(
            "Identifies medications, devices and any other substance used as part "
            "of the procedure."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device", "Medication", "Substance"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Procedure`` according specification,
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
            "instantiatesCanonical",
            "instantiatesUri",
            "basedOn",
            "partOf",
            "status",
            "statusReason",
            "category",
            "code",
            "subject",
            "encounter",
            "performedDateTime",
            "performedPeriod",
            "performedString",
            "performedAge",
            "performedRange",
            "recorder",
            "asserter",
            "performer",
            "location",
            "reasonCode",
            "reasonReference",
            "bodySite",
            "outcome",
            "report",
            "complication",
            "complicationDetail",
            "followUp",
            "note",
            "focalDevice",
            "usedReference",
            "usedCode",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1118(
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
    def validate_one_of_many_1118(
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
            "performed": [
                "performedAge",
                "performedDateTime",
                "performedPeriod",
                "performedRange",
                "performedString",
            ]
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


class ProcedureFocalDevice(backboneelement.BackboneElement):
    """
    Manipulated, implanted, or removed device.
    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """

    resource_type = Field("ProcedureFocalDevice", const=True)

    action: fhirtypes.CodeableConceptType = Field(
        None,
        alias="action",
        title="Kind of change to device",
        description=(
            "The kind of change that happened to the device during the procedure. "
            "See http://hl7.org/fhir/ValueSet/device-action"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="A kind of change that happened to the device during the procedure.",
        binding_strength="preferred",
        binding_uri="http://hl7.org/fhir/ValueSet/device-action",
    )

    manipulated: fhirtypes.ReferenceType = Field(
        ...,
        alias="manipulated",
        title="Device that was changed",
        description="The device that was manipulated (changed) during the procedure.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ProcedureFocalDevice`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "action", "manipulated"]


class ProcedurePerformer(backboneelement.BackboneElement):
    """
    The people who performed the procedure.
    Limited to "real" people rather than equipment.
    """

    resource_type = Field("ProcedurePerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="The reference to the practitioner",
        description="The practitioner who was involved in the procedure.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "Patient",
            "RelatedPerson",
            "Device",
        ],
    )

    function: fhirtypes.CodeableConceptType = Field(
        None,
        alias="function",
        title="Type of performance",
        description=(
            "Distinguishes the type of involvement of the performer in the "
            "procedure. For example, surgeon, anaesthetist, endoscopist. See "
            "http://hl7.org/fhir/ValueSet/performer-role"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="A code that identifies the role of a performer of the procedure.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/performer-role",
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title="Organization the device or practitioner was acting for",
        description="The organization the device or practitioner was acting on behalf of.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ProcedurePerformer`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "function",
            "actor",
            "onBehalfOf",
        ]
