from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class TemplateReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class ImageRequest(_message.Message):
    __slots__ = ["b64image"]
    B64IMAGE_FIELD_NUMBER: _ClassVar[int]
    b64image: str
    def __init__(self, b64image: _Optional[str] = ...) -> None: ...

class ImageReply(_message.Message):
    __slots__ = ["b64image"]
    B64IMAGE_FIELD_NUMBER: _ClassVar[int]
    b64image: str
    def __init__(self, b64image: _Optional[str] = ...) -> None: ...
