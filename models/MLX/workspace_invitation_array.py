# coding: utf-8

"""
    Multilogin X Profile Access Management API

    Multilogin X Profile Access Management API allows you to control everything related to permissions, workspaces, team members.

    The version of the OpenAPI document: 1.0.0
    Contact: support@multilogin.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from models.MLX.workspace_invitation import WorkspaceInvitation
from typing import Optional, Set
from typing_extensions import Self

class WorkspaceInvitationArray(BaseModel):
    """
    WorkspaceInvitationArray
    """ # noqa: E501
    invitations: Annotated[List[WorkspaceInvitation], Field(min_length=1, max_length=100)]
    total_count: StrictInt
    __properties: ClassVar[List[str]] = ["invitations", "total_count"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WorkspaceInvitationArray from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in invitations (list)
        _items = []
        if self.invitations:
            for _item_invitations in self.invitations:
                if _item_invitations:
                    _items.append(_item_invitations.to_dict())
            _dict['invitations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkspaceInvitationArray from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "invitations": [WorkspaceInvitation.from_dict(_item) for _item in obj["invitations"]] if obj.get("invitations") is not None else None,
            "total_count": obj.get("total_count")
        })
        return _obj


