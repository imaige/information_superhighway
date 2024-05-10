from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AiModelOutputRequest(_message.Message):
    __slots__ = ("photo_id", "image_comparison_run_id", "image_comparison_name", "image_comparison_datatype", "image_comparison_shape", "image_comparison_contents")
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_COMPARISON_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_COMPARISON_NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_COMPARISON_DATATYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_COMPARISON_SHAPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_COMPARISON_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    photo_id: int
    image_comparison_run_id: str
    image_comparison_name: str
    image_comparison_datatype: str
    image_comparison_shape: int
    image_comparison_contents: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, photo_id: _Optional[int] = ..., image_comparison_run_id: _Optional[str] = ..., image_comparison_name: _Optional[str] = ..., image_comparison_datatype: _Optional[str] = ..., image_comparison_shape: _Optional[int] = ..., image_comparison_contents: _Optional[_Iterable[bytes]] = ...) -> None: ...

class StatusReply(_message.Message):
    __slots__ = ("photo_id",)
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    photo_id: int
    def __init__(self, photo_id: _Optional[int] = ...) -> None: ...
