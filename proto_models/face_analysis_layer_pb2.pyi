from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FaceRekognitionModelOutputRequest(_message.Message):
    __slots__ = ("photo_id", "project_table_name", "age_range_low", "age_range_high", "smile_value", "smile_confidence", "eyeglasses_value", "eyeglasses_confidence", "sunglasses_value", "sunglasses_confidence", "gender_value", "gender_confidence", "beard_value", "beard_confidence", "mustache_value", "mustache_confidence", "eyes_open_value", "eyes_open_confidence", "mouth_open_value", "mouth_open_confidence", "emotion_happy_confidence", "emotion_angry_confidence", "emotion_disgusted_confidence", "emotion_fear_confidence", "emotion_calm_confidence", "emotion_sad_confidence", "emotion_surprised_confidence", "emotion_confused_confidence", "landmarks", "pose_roll", "pose_yaw", "pose_pitch", "quality_brightness", "quality_sharpness", "confidence", "face_occluded_value", "face_occluded_confidence", "eye_direction_yaw", "eye_direction_pitch", "eye_direction_confidence")
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_RANGE_LOW_FIELD_NUMBER: _ClassVar[int]
    AGE_RANGE_HIGH_FIELD_NUMBER: _ClassVar[int]
    SMILE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SMILE_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    EYEGLASSES_VALUE_FIELD_NUMBER: _ClassVar[int]
    EYEGLASSES_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    SUNGLASSES_VALUE_FIELD_NUMBER: _ClassVar[int]
    SUNGLASSES_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    GENDER_VALUE_FIELD_NUMBER: _ClassVar[int]
    GENDER_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    BEARD_VALUE_FIELD_NUMBER: _ClassVar[int]
    BEARD_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    MUSTACHE_VALUE_FIELD_NUMBER: _ClassVar[int]
    MUSTACHE_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    EYES_OPEN_VALUE_FIELD_NUMBER: _ClassVar[int]
    EYES_OPEN_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    MOUTH_OPEN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MOUTH_OPEN_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    EMOTION_HAPPY_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    EMOTION_ANGRY_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    EMOTION_DISGUSTED_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    EMOTION_FEAR_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    EMOTION_CALM_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    EMOTION_SAD_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    EMOTION_SURPRISED_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    EMOTION_CONFUSED_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    LANDMARKS_FIELD_NUMBER: _ClassVar[int]
    POSE_ROLL_FIELD_NUMBER: _ClassVar[int]
    POSE_YAW_FIELD_NUMBER: _ClassVar[int]
    POSE_PITCH_FIELD_NUMBER: _ClassVar[int]
    QUALITY_BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    QUALITY_SHARPNESS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    FACE_OCCLUDED_VALUE_FIELD_NUMBER: _ClassVar[int]
    FACE_OCCLUDED_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    EYE_DIRECTION_YAW_FIELD_NUMBER: _ClassVar[int]
    EYE_DIRECTION_PITCH_FIELD_NUMBER: _ClassVar[int]
    EYE_DIRECTION_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    photo_id: str
    project_table_name: str
    age_range_low: int
    age_range_high: int
    smile_value: bool
    smile_confidence: float
    eyeglasses_value: bool
    eyeglasses_confidence: float
    sunglasses_value: bool
    sunglasses_confidence: float
    gender_value: str
    gender_confidence: float
    beard_value: bool
    beard_confidence: float
    mustache_value: bool
    mustache_confidence: float
    eyes_open_value: bool
    eyes_open_confidence: float
    mouth_open_value: bool
    mouth_open_confidence: float
    emotion_happy_confidence: float
    emotion_angry_confidence: float
    emotion_disgusted_confidence: float
    emotion_fear_confidence: float
    emotion_calm_confidence: float
    emotion_sad_confidence: float
    emotion_surprised_confidence: float
    emotion_confused_confidence: float
    landmarks: _containers.RepeatedCompositeFieldContainer[Landmark]
    pose_roll: float
    pose_yaw: float
    pose_pitch: float
    quality_brightness: float
    quality_sharpness: float
    confidence: float
    face_occluded_value: bool
    face_occluded_confidence: float
    eye_direction_yaw: float
    eye_direction_pitch: float
    eye_direction_confidence: float
    def __init__(self, photo_id: _Optional[str] = ..., project_table_name: _Optional[str] = ..., age_range_low: _Optional[int] = ..., age_range_high: _Optional[int] = ..., smile_value: bool = ..., smile_confidence: _Optional[float] = ..., eyeglasses_value: bool = ..., eyeglasses_confidence: _Optional[float] = ..., sunglasses_value: bool = ..., sunglasses_confidence: _Optional[float] = ..., gender_value: _Optional[str] = ..., gender_confidence: _Optional[float] = ..., beard_value: bool = ..., beard_confidence: _Optional[float] = ..., mustache_value: bool = ..., mustache_confidence: _Optional[float] = ..., eyes_open_value: bool = ..., eyes_open_confidence: _Optional[float] = ..., mouth_open_value: bool = ..., mouth_open_confidence: _Optional[float] = ..., emotion_happy_confidence: _Optional[float] = ..., emotion_angry_confidence: _Optional[float] = ..., emotion_disgusted_confidence: _Optional[float] = ..., emotion_fear_confidence: _Optional[float] = ..., emotion_calm_confidence: _Optional[float] = ..., emotion_sad_confidence: _Optional[float] = ..., emotion_surprised_confidence: _Optional[float] = ..., emotion_confused_confidence: _Optional[float] = ..., landmarks: _Optional[_Iterable[_Union[Landmark, _Mapping]]] = ..., pose_roll: _Optional[float] = ..., pose_yaw: _Optional[float] = ..., pose_pitch: _Optional[float] = ..., quality_brightness: _Optional[float] = ..., quality_sharpness: _Optional[float] = ..., confidence: _Optional[float] = ..., face_occluded_value: bool = ..., face_occluded_confidence: _Optional[float] = ..., eye_direction_yaw: _Optional[float] = ..., eye_direction_pitch: _Optional[float] = ..., eye_direction_confidence: _Optional[float] = ...) -> None: ...

class Landmark(_message.Message):
    __slots__ = ("Type", "X", "Y")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Type: str
    X: float
    Y: float
    def __init__(self, Type: _Optional[str] = ..., X: _Optional[float] = ..., Y: _Optional[float] = ...) -> None: ...

class FaceStatusReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
