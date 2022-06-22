"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Locale(google.protobuf.message.Message):
    """区域标识
    gRPC头部:x-bili-locale-bin
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    C_LOCALE_FIELD_NUMBER: builtins.int
    S_LOCALE_FIELD_NUMBER: builtins.int
    SIM_CODE_FIELD_NUMBER: builtins.int
    TIMEZONE_FIELD_NUMBER: builtins.int
    @property
    def c_locale(self) -> global___LocaleIds:
        """App设置的locale"""
        pass
    @property
    def s_locale(self) -> global___LocaleIds:
        """系统默认的locale"""
        pass
    sim_code: typing.Text
    """sim卡的国家码+运营商码"""

    timezone: typing.Text
    """时区"""

    def __init__(self,
        *,
        c_locale: typing.Optional[global___LocaleIds] = ...,
        s_locale: typing.Optional[global___LocaleIds] = ...,
        sim_code: typing.Text = ...,
        timezone: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["c_locale",b"c_locale","s_locale",b"s_locale"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["c_locale",b"c_locale","s_locale",b"s_locale","sim_code",b"sim_code","timezone",b"timezone"]) -> None: ...
global___Locale = Locale

class LocaleIds(google.protobuf.message.Message):
    """Defined by https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LANGUAGE_FIELD_NUMBER: builtins.int
    SCRIPT_FIELD_NUMBER: builtins.int
    REGION_FIELD_NUMBER: builtins.int
    language: typing.Text
    """A language designator is a code that represents a language."""

    script: typing.Text
    """Writing systems."""

    region: typing.Text
    """A region designator is a code that represents a country or an area."""

    def __init__(self,
        *,
        language: typing.Text = ...,
        script: typing.Text = ...,
        region: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["language",b"language","region",b"region","script",b"script"]) -> None: ...
global___LocaleIds = LocaleIds
