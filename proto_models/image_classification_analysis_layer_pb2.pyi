from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ImageClassificationModelOutputRequest(_message.Message):
    __slots__ = ("project_table_name", "photo_id", "labels_from_classifications_model")
    PROJECT_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FROM_CLASSIFICATIONS_MODEL_FIELD_NUMBER: _ClassVar[int]
    project_table_name: str
    photo_id: int
    labels_from_classifications_model: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, project_table_name: _Optional[str] = ..., photo_id: _Optional[int] = ..., labels_from_classifications_model: _Optional[_Iterable[bytes]] = ...) -> None: ...

class ImageClassificationStatusReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
