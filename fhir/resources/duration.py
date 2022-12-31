# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Duration
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic import Field

from . import quantity


class Duration(quantity.Quantity):
    """
    A length of time.
    """

    resource_type = Field("Duration", const=True)

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Duration`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "value", "comparator", "unit", "system", "code"]
