from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FaceRekognitionModelOutputRequest(_message.Message):
    __slots__ = ("photo_id", "project_table_name", "age_range_low", "age_range_high", "smile_value", "smile_confidence", "eyeglasses_value", "eyeglasses_confidence", "sunglasses_value", "sunglasses_confidence", "gender_value", "gender_confidence", "beard_value", "beard_confidence", "mustache_value", "mustache_confidence", "eyes_open_value", "eyes_open_confidence", "mouth_open_value", "mouth_open_confidence", "emotion_happy_confidence", "emotion_angry_confidence", "emotion_disgusted_confidence", "emotion_fear_confidence", "emotion_calm_confidence", "emotion_sad_confidence", "emotion_surprised_confidence", "emotion_confused_confidence", "landmark_eye_left_x", "landmark_eye_left_y", "landmark_eye_right_x", "landmark_eye_right_y", "landmark_mouth_left_x", "landmark_mouth_left_y", "landmark_mouth_right_x", "landmark_mouth_right_y", "landmark_nose_x", "landmark_nose_y", "landmark_left_eyebrow_left_x", "landmark_left_eyebrow_left_y", "landmark_left_eyebrow_right_x", "landmark_left_eyebrow_right_y", "landmark_left_eyebrow_up_x", "landmark_left_eyebrow_up_y", "landmark_right_eyebrow_left_x", "landmark_right_eyebrow_left_y", "landmark_right_eyebrow_right_x", "landmark_right_eyebrow_right_y", "landmark_right_eyebrow_up_x", "landmark_right_eyebrow_up_y", "landmark_left_eye_left_x", "landmark_left_eye_left_y", "landmark_left_eye_right_x", "landmark_left_eye_right_y", "landmark_left_eye_up_x", "landmark_left_eye_up_y", "landmark_left_eye_down_x", "landmark_left_eye_down_y", "landmark_right_eye_left_x", "landmark_right_eye_left_y", "landmark_right_eye_right_x", "landmark_right_eye_right_y", "landmark_right_eye_up_x", "landmark_right_eye_up_y", "landmark_right_eye_down_x", "landmark_right_eye_down_y", "landmark_nose_left_x", "landmark_nose_left_y", "landmark_nose_right_x", "landmark_nose_right_y", "landmark_mouth_up_x", "landmark_mouth_up_y", "landmark_mouth_down_x", "landmark_mouth_down_y", "landmark_left_pupil_x", "landmark_left_pupil_y", "landmark_right_pupil_x", "landmark_right_pupil_y", "landmark_upper_jawline_left_x", "landmark_upper_jawline_left_y", "landmark_mid_jawline_left_x", "landmark_mid_jawline_left_y", "landmark_chin_bottom_x", "landmark_chin_bottom_y", "landmark_mid_jawline_right_x", "landmark_mid_jawline_right_y", "landmark_upper_jawline_right_x", "landmark_upper_jawline_right_y", "pose_roll", "pose_yaw", "pose_pitch", "quality_brightness", "quality_sharpness", "confidence", "face_occluded_value", "face_occluded_confidence", "eye_direction_yaw", "eye_direction_pitch", "eye_direction_confidence")
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
    LANDMARK_EYE_LEFT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_EYE_LEFT_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_EYE_RIGHT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_EYE_RIGHT_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_MOUTH_LEFT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_MOUTH_LEFT_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_MOUTH_RIGHT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_MOUTH_RIGHT_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_NOSE_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_NOSE_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_LEFT_EYEBROW_LEFT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_LEFT_EYEBROW_LEFT_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_LEFT_EYEBROW_RIGHT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_LEFT_EYEBROW_RIGHT_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_LEFT_EYEBROW_UP_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_LEFT_EYEBROW_UP_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_RIGHT_EYEBROW_LEFT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_RIGHT_EYEBROW_LEFT_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_RIGHT_EYEBROW_RIGHT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_RIGHT_EYEBROW_RIGHT_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_RIGHT_EYEBROW_UP_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_RIGHT_EYEBROW_UP_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_LEFT_EYE_LEFT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_LEFT_EYE_LEFT_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_LEFT_EYE_RIGHT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_LEFT_EYE_RIGHT_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_LEFT_EYE_UP_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_LEFT_EYE_UP_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_LEFT_EYE_DOWN_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_LEFT_EYE_DOWN_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_RIGHT_EYE_LEFT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_RIGHT_EYE_LEFT_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_RIGHT_EYE_RIGHT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_RIGHT_EYE_RIGHT_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_RIGHT_EYE_UP_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_RIGHT_EYE_UP_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_RIGHT_EYE_DOWN_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_RIGHT_EYE_DOWN_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_NOSE_LEFT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_NOSE_LEFT_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_NOSE_RIGHT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_NOSE_RIGHT_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_MOUTH_UP_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_MOUTH_UP_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_MOUTH_DOWN_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_MOUTH_DOWN_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_LEFT_PUPIL_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_LEFT_PUPIL_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_RIGHT_PUPIL_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_RIGHT_PUPIL_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_UPPER_JAWLINE_LEFT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_UPPER_JAWLINE_LEFT_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_MID_JAWLINE_LEFT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_MID_JAWLINE_LEFT_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_CHIN_BOTTOM_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_CHIN_BOTTOM_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_MID_JAWLINE_RIGHT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_MID_JAWLINE_RIGHT_Y_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_UPPER_JAWLINE_RIGHT_X_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_UPPER_JAWLINE_RIGHT_Y_FIELD_NUMBER: _ClassVar[int]
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
    landmark_eye_left_x: float
    landmark_eye_left_y: float
    landmark_eye_right_x: float
    landmark_eye_right_y: float
    landmark_mouth_left_x: float
    landmark_mouth_left_y: float
    landmark_mouth_right_x: float
    landmark_mouth_right_y: float
    landmark_nose_x: float
    landmark_nose_y: float
    landmark_left_eyebrow_left_x: float
    landmark_left_eyebrow_left_y: float
    landmark_left_eyebrow_right_x: float
    landmark_left_eyebrow_right_y: float
    landmark_left_eyebrow_up_x: float
    landmark_left_eyebrow_up_y: float
    landmark_right_eyebrow_left_x: float
    landmark_right_eyebrow_left_y: float
    landmark_right_eyebrow_right_x: float
    landmark_right_eyebrow_right_y: float
    landmark_right_eyebrow_up_x: float
    landmark_right_eyebrow_up_y: float
    landmark_left_eye_left_x: float
    landmark_left_eye_left_y: float
    landmark_left_eye_right_x: float
    landmark_left_eye_right_y: float
    landmark_left_eye_up_x: float
    landmark_left_eye_up_y: float
    landmark_left_eye_down_x: float
    landmark_left_eye_down_y: float
    landmark_right_eye_left_x: float
    landmark_right_eye_left_y: float
    landmark_right_eye_right_x: float
    landmark_right_eye_right_y: float
    landmark_right_eye_up_x: float
    landmark_right_eye_up_y: float
    landmark_right_eye_down_x: float
    landmark_right_eye_down_y: float
    landmark_nose_left_x: float
    landmark_nose_left_y: float
    landmark_nose_right_x: float
    landmark_nose_right_y: float
    landmark_mouth_up_x: float
    landmark_mouth_up_y: float
    landmark_mouth_down_x: float
    landmark_mouth_down_y: float
    landmark_left_pupil_x: float
    landmark_left_pupil_y: float
    landmark_right_pupil_x: float
    landmark_right_pupil_y: float
    landmark_upper_jawline_left_x: float
    landmark_upper_jawline_left_y: float
    landmark_mid_jawline_left_x: float
    landmark_mid_jawline_left_y: float
    landmark_chin_bottom_x: float
    landmark_chin_bottom_y: float
    landmark_mid_jawline_right_x: float
    landmark_mid_jawline_right_y: float
    landmark_upper_jawline_right_x: float
    landmark_upper_jawline_right_y: float
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
    def __init__(self, photo_id: _Optional[str] = ..., project_table_name: _Optional[str] = ..., age_range_low: _Optional[int] = ..., age_range_high: _Optional[int] = ..., smile_value: bool = ..., smile_confidence: _Optional[float] = ..., eyeglasses_value: bool = ..., eyeglasses_confidence: _Optional[float] = ..., sunglasses_value: bool = ..., sunglasses_confidence: _Optional[float] = ..., gender_value: _Optional[str] = ..., gender_confidence: _Optional[float] = ..., beard_value: bool = ..., beard_confidence: _Optional[float] = ..., mustache_value: bool = ..., mustache_confidence: _Optional[float] = ..., eyes_open_value: bool = ..., eyes_open_confidence: _Optional[float] = ..., mouth_open_value: bool = ..., mouth_open_confidence: _Optional[float] = ..., emotion_happy_confidence: _Optional[float] = ..., emotion_angry_confidence: _Optional[float] = ..., emotion_disgusted_confidence: _Optional[float] = ..., emotion_fear_confidence: _Optional[float] = ..., emotion_calm_confidence: _Optional[float] = ..., emotion_sad_confidence: _Optional[float] = ..., emotion_surprised_confidence: _Optional[float] = ..., emotion_confused_confidence: _Optional[float] = ..., landmark_eye_left_x: _Optional[float] = ..., landmark_eye_left_y: _Optional[float] = ..., landmark_eye_right_x: _Optional[float] = ..., landmark_eye_right_y: _Optional[float] = ..., landmark_mouth_left_x: _Optional[float] = ..., landmark_mouth_left_y: _Optional[float] = ..., landmark_mouth_right_x: _Optional[float] = ..., landmark_mouth_right_y: _Optional[float] = ..., landmark_nose_x: _Optional[float] = ..., landmark_nose_y: _Optional[float] = ..., landmark_left_eyebrow_left_x: _Optional[float] = ..., landmark_left_eyebrow_left_y: _Optional[float] = ..., landmark_left_eyebrow_right_x: _Optional[float] = ..., landmark_left_eyebrow_right_y: _Optional[float] = ..., landmark_left_eyebrow_up_x: _Optional[float] = ..., landmark_left_eyebrow_up_y: _Optional[float] = ..., landmark_right_eyebrow_left_x: _Optional[float] = ..., landmark_right_eyebrow_left_y: _Optional[float] = ..., landmark_right_eyebrow_right_x: _Optional[float] = ..., landmark_right_eyebrow_right_y: _Optional[float] = ..., landmark_right_eyebrow_up_x: _Optional[float] = ..., landmark_right_eyebrow_up_y: _Optional[float] = ..., landmark_left_eye_left_x: _Optional[float] = ..., landmark_left_eye_left_y: _Optional[float] = ..., landmark_left_eye_right_x: _Optional[float] = ..., landmark_left_eye_right_y: _Optional[float] = ..., landmark_left_eye_up_x: _Optional[float] = ..., landmark_left_eye_up_y: _Optional[float] = ..., landmark_left_eye_down_x: _Optional[float] = ..., landmark_left_eye_down_y: _Optional[float] = ..., landmark_right_eye_left_x: _Optional[float] = ..., landmark_right_eye_left_y: _Optional[float] = ..., landmark_right_eye_right_x: _Optional[float] = ..., landmark_right_eye_right_y: _Optional[float] = ..., landmark_right_eye_up_x: _Optional[float] = ..., landmark_right_eye_up_y: _Optional[float] = ..., landmark_right_eye_down_x: _Optional[float] = ..., landmark_right_eye_down_y: _Optional[float] = ..., landmark_nose_left_x: _Optional[float] = ..., landmark_nose_left_y: _Optional[float] = ..., landmark_nose_right_x: _Optional[float] = ..., landmark_nose_right_y: _Optional[float] = ..., landmark_mouth_up_x: _Optional[float] = ..., landmark_mouth_up_y: _Optional[float] = ..., landmark_mouth_down_x: _Optional[float] = ..., landmark_mouth_down_y: _Optional[float] = ..., landmark_left_pupil_x: _Optional[float] = ..., landmark_left_pupil_y: _Optional[float] = ..., landmark_right_pupil_x: _Optional[float] = ..., landmark_right_pupil_y: _Optional[float] = ..., landmark_upper_jawline_left_x: _Optional[float] = ..., landmark_upper_jawline_left_y: _Optional[float] = ..., landmark_mid_jawline_left_x: _Optional[float] = ..., landmark_mid_jawline_left_y: _Optional[float] = ..., landmark_chin_bottom_x: _Optional[float] = ..., landmark_chin_bottom_y: _Optional[float] = ..., landmark_mid_jawline_right_x: _Optional[float] = ..., landmark_mid_jawline_right_y: _Optional[float] = ..., landmark_upper_jawline_right_x: _Optional[float] = ..., landmark_upper_jawline_right_y: _Optional[float] = ..., pose_roll: _Optional[float] = ..., pose_yaw: _Optional[float] = ..., pose_pitch: _Optional[float] = ..., quality_brightness: _Optional[float] = ..., quality_sharpness: _Optional[float] = ..., confidence: _Optional[float] = ..., face_occluded_value: bool = ..., face_occluded_confidence: _Optional[float] = ..., eye_direction_yaw: _Optional[float] = ..., eye_direction_pitch: _Optional[float] = ..., eye_direction_confidence: _Optional[float] = ...) -> None: ...

class FaceStatusReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
