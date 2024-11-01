from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ImageAnalysisRequest(_message.Message):
    __slots__ = ("photo_id", "project_table_name", "b64image", "models")
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    B64IMAGE_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    photo_id: int
    project_table_name: str
    b64image: str
    models: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, photo_id: _Optional[int] = ..., project_table_name: _Optional[str] = ..., b64image: _Optional[str] = ..., models: _Optional[_Iterable[str]] = ...) -> None: ...

class ImageAnalysisResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class SuperhighwayStatusReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
