from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ImageAnalysisRequest(_message.Message):
    __slots__ = ("b64image", "model_name")
    B64IMAGE_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    b64image: str
    model_name: str
    def __init__(self, b64image: _Optional[str] = ..., model_name: _Optional[str] = ...) -> None: ...

class StatusReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
