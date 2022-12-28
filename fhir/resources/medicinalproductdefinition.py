# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductDefinition
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


class MedicinalProductDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Detailed definition of a medicinal product.
    A medicinal product, being a substance or combination of substances that is
    intended to treat, prevent or diagnose a disease, or to restore, correct or
    modify physiological functions by exerting a pharmacological, immunological
    or metabolic action. This resource is intended to define and detail such
    products and their properties, for uses other than direct patient care
    (e.g. regulatory use, or drug catalogs).
    """

    resource_type = Field("MedicinalProductDefinition", const=True)

    additionalMonitoringIndicator: fhirtypes.CodeableConceptType = Field(
        None,
        alias="additionalMonitoringIndicator",
        title=(
            "Whether the Medicinal Product is subject to additional monitoring for "
            "regulatory reasons"
        ),
        description=(
            "Whether the Medicinal Product is subject to additional monitoring for "
            "regulatory reasons, such as heightened reporting requirements. See "
            "http://hl7.org/fhir/ValueSet/medicinal-product-additional-monitoring"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Extra measures defined for a Medicinal Product, such as heightened reporting requirements (e.g. Black Triangle Monitoring).",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/medicinal-product-additional-monitoring",
    )

    attachedDocument: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="attachedDocument",
        title="Additional documentation about the medicinal product",
        description=(
            "Additional information or supporting documentation about the medicinal"
            " product."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
        backref="medicinal_product_definition",
        parent_name="medicinal_product_definition",
    )

    characteristic: typing.List[
        fhirtypes.MedicinalProductDefinitionCharacteristicType
    ] = Field(
        None,
        alias="characteristic",
        title='Key product features such as "sugar free", "modified release"',
        description=(
            'Allows the key product features to be recorded, such as "sugar free", '
            '"modified release", "parallel import".'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    classification: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classification",
        title="Allows the product to be classified by various systems",
        description=(
            "Allows the product to be classified by various systems, commonly WHO "
            "ATC. See http://hl7.org/fhir/ValueSet/product-classification-codes"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="This value set includes codes from the Anatomical Therapeutic Chemical Classification System - provided as an exemplar value set.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/product-classification-codes",
    )

    clinicalTrial: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="clinicalTrial",
        title="Clinical trials or studies that this product is involved in",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ResearchStudy"],
        backref="medicinal_product_definition",
        parent_name="medicinal_product_definition",
    )

    code: typing.List[fhirtypes.CodingType] = Field(
        None,
        alias="code",
        title="A code that this product is known by, within some formal terminology",
        description=(
            "A code that this product is known by, usually within some formal "
            "terminology, perhaps assigned by a third party (i.e. not the "
            "manufacturer or regulator). Products (types of medications) tend to be"
            " known by identifiers during development and within regulatory "
            "process. However when they are prescribed they tend to be identified "
            "by codes. The same product may be have multiple codes, applied to it "
            "by multiple organizations. See "
            "http://hl7.org/fhir/ValueSet/medication-codes"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="A coded concept that defines the type of a medication.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/medication-codes",
    )

    combinedPharmaceuticalDoseForm: fhirtypes.CodeableConceptType = Field(
        None,
        alias="combinedPharmaceuticalDoseForm",
        title=(
            "The dose form for a single part product, or combined form of a "
            "multiple part product"
        ),
        description=(
            "The dose form for a single part product, or combined form of a "
            "multiple part product. This is one concept that describes all the "
            "components. It does not represent the form with components physically "
            "mixed, if that might be necessary, for which see "
            "(AdministrableProductDefinition.administrableDoseForm). See "
            "http://hl7.org/fhir/ValueSet/combined-dose-form"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Dose forms for a product as a whole, considering all individual parts, but before any mixing",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/combined-dose-form",
    )

    contact: typing.List[fhirtypes.MedicinalProductDefinitionContactType] = Field(
        None,
        alias="contact",
        title="A product specific contact, person (in a role), or an organization",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    crossReference: typing.List[
        fhirtypes.MedicinalProductDefinitionCrossReferenceType
    ] = Field(
        None,
        alias="crossReference",
        title=(
            "Reference to another product, e.g. for linking authorised to "
            "investigational product"
        ),
        description=(
            "Reference to another product, e.g. for linking authorised to "
            "investigational product, or a virtual product."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="General description of this product",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    domain: fhirtypes.CodeableConceptType = Field(
        None,
        alias="domain",
        title="If this medicine applies to human or veterinary uses",
        description="See http://hl7.org/fhir/ValueSet/medicinal-product-domain",
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Applicable domain for this product (e.g. human, veterinary).",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/medicinal-product-domain",
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier for this product. Could be an MPID",
        description=(
            "Business identifier for this product. Could be an MPID. When in "
            "development or being regulated, products are typically referenced by "
            "official identifiers, assigned by a manufacturer or regulator, and "
            "unique to a product (which, when compared to a product instance being "
            "prescribed, is actually a product type). See also "
            "MedicinalProductDefinition.code."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    impurity: typing.List[fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="impurity",
        title=(
            "Any component of the drug product which is not the chemical entity "
            "defined as the drug substance, or an excipient in the drug product"
        ),
        description=(
            "Any component of the drug product which is not the chemical entity "
            "defined as the drug substance, or an excipient in the drug product. "
            "This includes process-related impurities and contaminants, product-"
            "related impurities including degradation products. See "
            "http://hl7.org/fhir/ValueSet/substance-codes"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="This value set includes all substance codes from SNOMED CT - provided as an exemplar value set.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/substance-codes",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SubstanceDefinition"],
        backref="medicinal_product_definition",
        parent_name="medicinal_product_definition",
    )

    indication: fhirtypes.Markdown = Field(
        None,
        alias="indication",
        title=(
            "Description of indication(s) for this product, used when structured "
            "indications are not required"
        ),
        description=(
            "Description of indication(s) for this product, used when structured "
            "indications are not required. In cases where structured indications "
            "are required, they are captured using the ClinicalUseDefinition "
            "resource. An indication is a medical situation for which using the "
            "product is appropriate."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    indication__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_indication", title="Extension field for ``indication``."
    )

    ingredient: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="ingredient",
        title=(
            "The ingredients of this medicinal product - when not detailed in other"
            " resources"
        ),
        description=(
            "The ingredients of this medicinal product - when not detailed in other"
            " resources. This is only needed if the ingredients are not specified "
            "by incoming references from the Ingredient resource, or indirectly via"
            " incoming AdministrableProductDefinition, PackagedProductDefinition or"
            " ManufacturedItemDefinition references. In cases where those levels of"
            " detail are not used, the ingredients may be specified directly here "
            "as codes. See http://hl7.org/fhir/ValueSet/substance-codes"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="This value set includes all substance codes from SNOMED CT - provided as an exemplar value set.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/substance-codes",
    )

    legalStatusOfSupply: fhirtypes.CodeableConceptType = Field(
        None,
        alias="legalStatusOfSupply",
        title=(
            "The legal status of supply of the medicinal product as classified by "
            "the regulator"
        ),
        description="See http://hl7.org/fhir/ValueSet/legal-status-of-supply",
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="The prescription supply types appropriate to a medicinal product",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/legal-status-of-supply",
    )

    marketingStatus: typing.List[fhirtypes.MarketingStatusType] = Field(
        None,
        alias="marketingStatus",
        title=(
            "Marketing status of the medicinal product, in contrast to marketing "
            "authorization"
        ),
        description=(
            "Marketing status of the medicinal product, in contrast to marketing "
            "authorization. This refers to the product being actually 'on the "
            "market' as opposed to being allowed to be on the market (which is an "
            "authorization)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    masterFile: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="masterFile",
        title=(
            "A master file for the medicinal product (e.g. Pharmacovigilance System"
            " Master File)"
        ),
        description=(
            "A master file for the medicinal product (e.g. Pharmacovigilance System"
            " Master File). Drug master files (DMFs) are documents submitted to "
            "regulatory agencies to provide confidential detailed information about"
            " facilities, processes or articles used in the manufacturing, "
            "processing, packaging and storing of drug products."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
        backref="medicinal_product_definition",
        parent_name="medicinal_product_definition",
    )

    name: typing.List[fhirtypes.MedicinalProductDefinitionNameType] = Field(
        ...,
        alias="name",
        title="The product's name, including full name and possibly coded parts",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    operation: typing.List[fhirtypes.MedicinalProductDefinitionOperationType] = Field(
        None,
        alias="operation",
        title="A manufacturing or administrative process for the medicinal product",
        description=(
            "A manufacturing or administrative process or step associated with (or "
            "performed on) the medicinal product."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    packagedMedicinalProduct: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="packagedMedicinalProduct",
        title="Package type for the product",
        description=(
            "Package type for the product. See also the PackagedProductDefinition "
            "resource. See http://hl7.org/fhir/ValueSet/medicinal-product-package-"
            "type"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Types of medicinal product packs",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/medicinal-product-package-type",
    )

    pediatricUseIndicator: fhirtypes.CodeableConceptType = Field(
        None,
        alias="pediatricUseIndicator",
        title="If authorised for use in children",
        description=(
            "If authorised for use in children, or infants, neonates etc. See "
            "http://hl7.org/fhir/ValueSet/medicinal-product-pediatric-use"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Suitability for age groups, in particular children.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/medicinal-product-pediatric-use",
    )

    route: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="route",
        title=(
            "The path by which the product is taken into or makes contact with the "
            "body"
        ),
        description=(
            "The path by which the product is taken into or makes contact with the "
            "body. In some regions this is referred to as the licenced or approved "
            "route. See also AdministrableProductDefinition resource. "
            "MedicinalProductDefinition.route is the same concept as "
            "AdministrableProductDefinition.routeOfAdministration.code, and they "
            "cannot be used together. See http://hl7.org/fhir/ValueSet/route-codes"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="A code specifying the route or physiological path of administration of a therapeutic agent into or onto a patient\u0027s body.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/route-codes",
    )

    specialMeasures: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialMeasures",
        title=(
            "Whether the Medicinal Product is subject to special measures for "
            "regulatory reasons"
        ),
        description=(
            "Whether the Medicinal Product is subject to special measures for "
            "regulatory reasons, such as a requirement to conduct post-"
            "authorisation studies. See http://hl7.org/fhir/ValueSet/medicinal-"
            "product-special-measures"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Extra measures defined for a Medicinal Product, such as a requirement to conduct post-authorisation studies.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/medicinal-product-special-measures",
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="The status within the lifecycle of this product record",
        description=(
            "The status within the lifecycle of this product record. A high-level "
            "status, this is not intended to duplicate details carried elsewhere "
            "such as legal status, or authorization status. See "
            "http://hl7.org/fhir/ValueSet/publication-status"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="The lifecycle status of an artifact.",
        binding_strength="preferred",
        binding_uri="http://hl7.org/fhir/ValueSet/publication-status",
    )

    statusDate: fhirtypes.DateTime = Field(
        None,
        alias="statusDate",
        title="The date at which the given status became applicable",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_statusDate", title="Extension field for ``statusDate``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Regulatory type, e.g. Investigational or Authorized",
        description="See http://hl7.org/fhir/ValueSet/medicinal-product-type",
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Overall defining type of this medicinal product.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/medicinal-product-type",
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="A business identifier relating to a specific version of the product",
        description=(
            "A business identifier relating to a specific version of the product, "
            "this is commonly used to support revisions to an existing product."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicinalProductDefinition`` according specification,
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
            "type",
            "domain",
            "version",
            "status",
            "statusDate",
            "description",
            "combinedPharmaceuticalDoseForm",
            "route",
            "indication",
            "legalStatusOfSupply",
            "additionalMonitoringIndicator",
            "specialMeasures",
            "pediatricUseIndicator",
            "classification",
            "marketingStatus",
            "packagedMedicinalProduct",
            "ingredient",
            "impurity",
            "attachedDocument",
            "masterFile",
            "contact",
            "clinicalTrial",
            "code",
            "name",
            "crossReference",
            "operation",
            "characteristic",
        ]


class MedicinalProductDefinitionCharacteristic(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Key product features such as "sugar free", "modified release".
    Allows the key product features to be recorded, such as "sugar free",
    "modified release", "parallel import".
    """

    resource_type = Field("MedicinalProductDefinitionCharacteristic", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="A code expressing the type of characteristic",
        description="See http://hl7.org/fhir/ValueSet/product-characteristic-codes",
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="This value set includes all observable entity codes from SNOMED CT - provided as an exemplar value set.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/product-characteristic-codes",
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    valueDate: fhirtypes.Date = Field(
        None,
        alias="valueDate",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="A value for the characteristic",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicinalProductDefinitionCharacteristic`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "valueCodeableConcept",
            "valueQuantity",
            "valueDate",
            "valueBoolean",
            "valueAttachment",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4297(
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
            "value": [
                "valueAttachment",
                "valueBoolean",
                "valueCodeableConcept",
                "valueDate",
                "valueQuantity",
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


class MedicinalProductDefinitionContact(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A product specific contact, person (in a role), or an organization.
    """

    resource_type = Field("MedicinalProductDefinitionContact", const=True)

    contact: fhirtypes.ReferenceType = Field(
        ...,
        alias="contact",
        title="A product specific contact, person (in a role), or an organization",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization", "PractitionerRole"],
        backref="medicinal_product_definition_contact",
        parent_name="medicinal_product_definition_contact",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "Allows the contact to be classified, for example QPPV, "
            "Pharmacovigilance Enquiry Information"
        ),
        description="See http://hl7.org/fhir/ValueSet/medicinal-product-contact-type",
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Extra measures defined for a Medicinal Product, such as heightened reporting requirements.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/medicinal-product-contact-type",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicinalProductDefinitionContact`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "contact"]


class MedicinalProductDefinitionCrossReference(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Reference to another product, e.g. for linking authorised to
    investigational product.
    Reference to another product, e.g. for linking authorised to
    investigational product, or a virtual product.
    """

    resource_type = Field("MedicinalProductDefinitionCrossReference", const=True)

    product: fhirtypes.CodeableReferenceType = Field(
        ...,
        alias="product",
        title=(
            "Reference to another product, e.g. for linking authorised to "
            "investigational product"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProductDefinition"],
        backref="medicinal_product_definition_cross_reference",
        parent_name="medicinal_product_definition_cross_reference",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "The type of relationship, for instance branded to generic or virtual "
            "to actual product"
        ),
        description=(
            "The type of relationship, for instance branded to generic, virtual to "
            "actual product, product to development product (investigational), "
            "parallel import version. See http://hl7.org/fhir/ValueSet/medicinal-"
            "product-cross-reference-type"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Extra measures defined for a Medicinal Product, such as heightened reporting requirements.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/medicinal-product-cross-reference-type",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicinalProductDefinitionCrossReference`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "product", "type"]


class MedicinalProductDefinitionName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The product's name, including full name and possibly coded parts.
    """

    resource_type = Field("MedicinalProductDefinitionName", const=True)

    countryLanguage: typing.List[
        fhirtypes.MedicinalProductDefinitionNameCountryLanguageType
    ] = Field(
        None,
        alias="countryLanguage",
        title="Country and jurisdiction where the name applies",
        description=(
            "Country and jurisdiction where the name applies, and associated "
            "language."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    namePart: typing.List[fhirtypes.MedicinalProductDefinitionNameNamePartType] = Field(
        None,
        alias="namePart",
        title="Coding words or phrases of the name",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    productName: fhirtypes.String = Field(
        None,
        alias="productName",
        title="The full product name",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    productName__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_productName", title="Extension field for ``productName``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type of product name, such as rINN, BAN, Proprietary, Non-Proprietary",
        description="See http://hl7.org/fhir/ValueSet/medicinal-product-name-type",
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Type of a name for a Medicinal Product.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/medicinal-product-name-type",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicinalProductDefinitionName`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "productName",
            "type",
            "namePart",
            "countryLanguage",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_3235(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("productName", "productName__ext")]
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


class MedicinalProductDefinitionNameCountryLanguage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Country and jurisdiction where the name applies.
    Country and jurisdiction where the name applies, and associated language.
    """

    resource_type = Field("MedicinalProductDefinitionNameCountryLanguage", const=True)

    country: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="country",
        title="Country code for where this name applies",
        description="See http://hl7.org/fhir/ValueSet/country",
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Jurisdiction codes",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/country",
    )

    jurisdiction: fhirtypes.CodeableConceptType = Field(
        None,
        alias="jurisdiction",
        title="Jurisdiction code for where this name applies",
        description=(
            "Jurisdiction code for where this name applies. A jurisdiction may be a"
            " sub- or supra-national entity (e.g. a state or a geographic region). "
            "See http://hl7.org/fhir/ValueSet/jurisdiction"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Jurisdiction codes",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/jurisdiction",
    )

    language: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="language",
        title="Language code for this name",
        description="See http://hl7.org/fhir/ValueSet/languages",
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="IETF language tag",
        binding_strength="preferred",
        binding_uri="http://hl7.org/fhir/ValueSet/languages",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicinalProductDefinitionNameCountryLanguage`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "country",
            "jurisdiction",
            "language",
        ]


class MedicinalProductDefinitionNameNamePart(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Coding words or phrases of the name.
    """

    resource_type = Field("MedicinalProductDefinitionNameNamePart", const=True)

    part: fhirtypes.String = Field(
        None,
        alias="part",
        title="A fragment of a product name",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    part__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_part", title="Extension field for ``part``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Identifying type for this part of the name (e.g. strength part)",
        description="See http://hl7.org/fhir/ValueSet/medicinal-product-name-part-type",
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Type of part of a name for a Medicinal Product.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/medicinal-product-name-part-type",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicinalProductDefinitionNameNamePart`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "part", "type"]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_4042(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("part", "part__ext")]
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


class MedicinalProductDefinitionOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A manufacturing or administrative process for the medicinal product.
    A manufacturing or administrative process or step associated with (or
    performed on) the medicinal product.
    """

    resource_type = Field("MedicinalProductDefinitionOperation", const=True)

    confidentialityIndicator: fhirtypes.CodeableConceptType = Field(
        None,
        alias="confidentialityIndicator",
        title=(
            "Specifies whether this process is considered proprietary or "
            "confidential"
        ),
        description=(
            "Specifies whether this particular business or manufacturing process is"
            " considered proprietary or confidential. See "
            "http://hl7.org/fhir/ValueSet/medicinal-product-confidentiality"
        ),
        # if property is element of this resource.
        element_property=True,
        # valueset binding
        binding_description="Confidentiality rating, e.g. commercial sensitivity for a Medicinal Product.",
        binding_strength="example",
        binding_uri="http://hl7.org/fhir/ValueSet/medicinal-product-confidentiality",
    )

    effectiveDate: fhirtypes.PeriodType = Field(
        None,
        alias="effectiveDate",
        title="Date range of applicability",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    organization: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="organization",
        title=(
            "The organization responsible for the particular process, e.g. the "
            "manufacturer or importer"
        ),
        description=(
            "The organization or establishment responsible for (or associated with)"
            " the particular process or step, examples include the manufacturer, "
            "importer, agent."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
        backref="medicinal_product_definition_operation",
        parent_name="medicinal_product_definition_operation",
    )

    type: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="type",
        title=(
            "The type of manufacturing operation e.g. manufacturing itself, re-"
            "packaging"
        ),
        description=(
            "The type of manufacturing operation e.g. manufacturing itself, re-"
            "packaging. For the authorization of this, a RegulatedAuthorization "
            "would point to the same plan or activity referenced here."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ActivityDefinition", "PlanDefinition"],
        backref="medicinal_product_definition_operation",
        parent_name="medicinal_product_definition_operation",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MedicinalProductDefinitionOperation`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "effectiveDate",
            "organization",
            "confidentialityIndicator",
        ]
