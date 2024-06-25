from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AiModelOutputRequest(_message.Message):
    __slots__ = ("photo_id", "image_comparison_run_id", "image_comparison_name", "image_comparison_datatype", "image_comparison_shape", "average_hash", "perceptual_hash", "difference_hash", "wavelet_hash_haar", "color_hash", "color_averages", "bounding_boxes_from_faces_model", "labels_from_classification_model")
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_COMPARISON_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_COMPARISON_NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_COMPARISON_DATATYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_COMPARISON_SHAPE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_HASH_FIELD_NUMBER: _ClassVar[int]
    PERCEPTUAL_HASH_FIELD_NUMBER: _ClassVar[int]
    DIFFERENCE_HASH_FIELD_NUMBER: _ClassVar[int]
    WAVELET_HASH_HAAR_FIELD_NUMBER: _ClassVar[int]
    COLOR_HASH_FIELD_NUMBER: _ClassVar[int]
    COLOR_AVERAGES_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOXES_FROM_FACES_MODEL_FIELD_NUMBER: _ClassVar[int]
    LABELS_FROM_CLASSIFICATION_MODEL_FIELD_NUMBER: _ClassVar[int]
    photo_id: int
    image_comparison_run_id: str
    image_comparison_name: str
    image_comparison_datatype: str
    image_comparison_shape: int
    average_hash: bytes
    perceptual_hash: bytes
    difference_hash: bytes
    wavelet_hash_haar: bytes
    color_hash: bytes
    color_averages: str
    bounding_boxes_from_faces_model: int
    labels_from_classification_model: int
    def __init__(self, photo_id: _Optional[int] = ..., image_comparison_run_id: _Optional[str] = ..., image_comparison_name: _Optional[str] = ..., image_comparison_datatype: _Optional[str] = ..., image_comparison_shape: _Optional[int] = ..., average_hash: _Optional[bytes] = ..., perceptual_hash: _Optional[bytes] = ..., difference_hash: _Optional[bytes] = ..., wavelet_hash_haar: _Optional[bytes] = ..., color_hash: _Optional[bytes] = ..., color_averages: _Optional[str] = ..., bounding_boxes_from_faces_model: _Optional[int] = ..., labels_from_classification_model: _Optional[int] = ...) -> None: ...

class StatusReply(_message.Message):
    __slots__ = ("photo_id",)
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    photo_id: int
    def __init__(self, photo_id: _Optional[int] = ...) -> None: ...
