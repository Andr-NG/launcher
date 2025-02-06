# coding: utf-8

"""
    Multilogin X Launcher API

    Launcher API is used to work with profiles in the browser (start, stop, get statuses).

    The version of the OpenAPI document: 1.0.0
    Contact: support@multilogin.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class MaskingCM(str, Enum):
    """
    MaskingCM
    """

    """
    allowed enum values
    """
    CUSTOM = 'custom'
    MASK = 'mask'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MaskingCM from a JSON string"""
        return cls(json.loads(json_str))


