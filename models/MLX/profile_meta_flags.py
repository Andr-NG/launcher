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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from models.MLX.masking_cd import MaskingCD
from models.MLX.masking_cm import MaskingCM
from models.MLX.masking_mn import MaskingMN
from models.MLX.masking_mnd import MaskingMND
from models.MLX.masking_ncm import MaskingNCM
from models.MLX.masking_ncmd import MaskingNCMD
from models.MLX.masking_nd import MaskingND
from models.MLX.masking_pab import MaskingPAB
from models.MLX.startup_behavior import StartupBehavior
from typing import Optional, Set
from typing_extensions import Self

class ProfileMetaFlags(BaseModel):
    """
    ProfileMetaFlags
    """ # noqa: E501
    navigator_masking: MaskingNCM
    audio_masking: MaskingMN
    localization_masking: MaskingNCM
    geolocation_popup: MaskingPAB
    geolocation_masking: MaskingCM
    timezone_masking: MaskingNCM
    graphics_noise: MaskingMN
    canvas_noise: Optional[MaskingMND] = None
    graphics_masking: MaskingNCM
    webrtc_masking: MaskingNCMD
    fonts_masking: MaskingNCM
    media_devices_masking: MaskingNCM
    screen_masking: MaskingNCM
    proxy_masking: MaskingCD
    ports_masking: MaskingMN
    quic_mode: Optional[MaskingND] = None
    startup_behavior: Optional[StartupBehavior] = None
    __properties: ClassVar[List[str]] = ["navigator_masking", "audio_masking", "localization_masking", "geolocation_popup", "geolocation_masking", "timezone_masking", "graphics_noise", "canvas_noise", "graphics_masking", "webrtc_masking", "fonts_masking", "media_devices_masking", "screen_masking", "proxy_masking", "ports_masking", "quic_mode", "startup_behavior"]

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
        """Create an instance of ProfileMetaFlags from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProfileMetaFlags from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "navigator_masking": obj.get("navigator_masking"),
            "audio_masking": obj.get("audio_masking"),
            "localization_masking": obj.get("localization_masking"),
            "geolocation_popup": obj.get("geolocation_popup"),
            "geolocation_masking": obj.get("geolocation_masking"),
            "timezone_masking": obj.get("timezone_masking"),
            "graphics_noise": obj.get("graphics_noise"),
            "canvas_noise": obj.get("canvas_noise"),
            "graphics_masking": obj.get("graphics_masking"),
            "webrtc_masking": obj.get("webrtc_masking"),
            "fonts_masking": obj.get("fonts_masking"),
            "media_devices_masking": obj.get("media_devices_masking"),
            "screen_masking": obj.get("screen_masking"),
            "proxy_masking": obj.get("proxy_masking"),
            "ports_masking": obj.get("ports_masking"),
            "quic_mode": obj.get("quic_mode"),
            "startup_behavior": obj.get("startup_behavior")
        })
        return _obj


