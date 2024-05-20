from enum import Enum as enum


# Enums
class AccountType(enum):
    USER = 1
    ADMIN = 2
    COMPANY_OWNER = 3
    MEDIAVIZ_INTERNAL_SUPER_ADMIN = 4


class AiModel(enum):
    face_detect_model = 'face_detect_model'
    image_classification_model = 'image_classification_model'
    colors_basic_model = 'colors_basic_model'
    image_comparison_hash_model = 'image_comparison_hash_model'

