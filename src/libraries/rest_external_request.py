import requests
from typing import Dict, Union, List
import logging

from requests import JSONDecodeError

from logging_file_format import configure_logger, get_log_level
import json
from os import getenv, path, listdir
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
log_level = get_log_level()
configure_logger(logger, level=log_level)

load_dotenv()


def request(url: str, request_type: str, headers: Union[Dict, None]):
    response = ''

    if request_type == 'get':
        response = requests.get(url, headers=headers)
    elif request_type == 'post':
        response = requests.post(url, headers=headers)

    response_json = response.json()
    # logger.info(f"Request {response.status_code}: {response_json}")
    return response_json


def request_with_body(url: str, obj: Dict, request_type: str, headers: Union[Dict, None]):
    response = ''

    if request_type == 'get':
        response = requests.get(url, json=obj, headers=headers)
    elif request_type == 'post':
        response = requests.post(url, json=obj, headers=headers)

    response_json = response.json()
    # logger.info(f"Request with body {response.status_code}: {response_json}")
    return response_json


def request_with_body_ssl_secured(url: str, obj: Dict, request_type: str, headers: Union[Dict, None]):
    response = ''

    if request_type == 'get':
        response = requests.get(url, json=obj, headers=headers)
    elif request_type == 'post':
        response = requests.post(url, json=obj, headers=headers)

    response_json = response.json()
    # logger.info(f"Request with body {response.status_code}: {response_json}")
    return response_json


def request_with_photo(url: str, request_type: str, heads: Union[Dict, None], photo_path: str):
    response = ''

    with open(photo_path, 'rb') as photo_file:
        photo_data = photo_file.read()
    files = [("photo", photo_data)]

    if request_type == 'get':
        response = requests.get(url, headers=heads)
    elif request_type == 'post':
        response = requests.post(url, files=files, headers=heads)

    try:
        response_json = response.json()
        logger.info(f"Request with body {response.status_code}: {response_json}")
        return response_json
    except JSONDecodeError as e:
        print(f"Caught error: {e}")


def request_with_body_and_photo(url: str, recipe: Union[List[str], None], request_type: str, heads: Union[Dict, None], photo_path: str):
    response = ''

    with open(photo_path, 'rb') as photo_file:
        photo_data = photo_file.read()

    files = [("photo", photo_data)]

    if request_type == 'get':
        response = requests.get(url, data=recipe, headers=heads)
    elif request_type == 'post':
        response = requests.post(url, data=recipe, files=files, headers=heads)

    try:
        response_json = response.json()
        logger.info(f"Request with body {response.status_code}: {response_json}")
        return response_json
    except JSONDecodeError as e:
        print(f"Caught error: {e}")


if __name__ == '__main__':
    # server_target = 'local'
    server_target = 'dev'
    # server_target = 'qa'
    # server_target = 'dev_similarity'
    # server_target = 'qa_test'

    photo_and_model = True

    table_name = ''
    if server_target == 'local':
        table_name = "z_1_9a8db925-52fc-404c-839d-b9c8830d6256_photos"
        if photo_and_model:
            url = "http://localhost:8000/api/v1/photos/model_request"
        else:
            url = "http://localhost:8000/api/v1/photos/"
    elif server_target == 'dev':
        table_name = "z_1_9a8db925-52fc-404c-839d-b9c8830d6256_photos"
        if photo_and_model:
            url = "https://dev.api.mediaviz.ai/api/v1/photos/model_request"
        else:
            url = "https://dev.api.mediaviz.ai/api/v1/photos/"
    elif server_target == 'dev_similarity':
        # table_name = "z_1_6031746f-b9f4-4588-bb1d-5f7a817f06c2_photos"
        # table_name = "z_1_20033e5a-a636-4fa7-9d3a-4175d4ff41f1_photos"
        table_name = "z_1_c75e6b01-883c-44ce-95e0-7da154e67059_photos"
        if photo_and_model:
            url = "https://dev.api.mediaviz.ai/api/v1/photos/model_request"
        else:
            url = "https://dev.api.mediaviz.ai/api/v1/photos/"
    elif server_target == 'qa':
        table_name = "z_2_688cf6a4-7a24-4bd5-84fc-e9789861b558_photos"
        if photo_and_model:
            url = "https://api.mediaviz.ai/api/v1/photos/model_request"
        else:
            url = "https://api.mediaviz.ai/api/v1/photos/"
    elif server_target == 'qa_test':
        table_name = "z_2_242f0947-d1eb-43ff-8a32-5697757f2d18_photos"
        if photo_and_model:
            url = "https://api.mediaviz.ai/api/v1/photos/model_request"
        else:
            url = "https://api.mediaviz.ai/api/v1/photos/"

    recipe = {
        "name": "test-recipe",
        "description": "describe me",
        "table_name": table_name,  # dev
        "models": [
            "image_comparison_hash_model",
            # "colors_basic_model",
            "image_classification_model",
            # "face_detect_model",
            # "blur_model",
            # "feature_extraction_model",
            # "image_comparison_test_model"
        ],
        "date_taken": '2024-10-15',
        "client_side_id": 'test-id-unique'
    }

    token = ""

    token_body = {
        "name": "Test1 User1",
        "email": "test1@example.com",
        "password": "Password1!",
        "profile_picture": "test1.jpg",
        "account_type": 1,
        "company_id": 1
    }

    # k8s dev raw url
    # k8s photo ai request
    # url = "http://a2dfc76eee74e458ba52f9438dae0f4c-176970126.us-east-2.elb.amazonaws.com:443/api/v1/photos/model_request"

    # token
    # url = "http://acb5bb47a60054e3ab8f6f2bab81a51c-1018561966.us-east-2.elb.amazonaws.com:80/api/v1/token"

    if url[8:11] == "dev" or url[0:5] == "http:":
        token = getenv("K8S_DEV_EXTERNAL_API_BEARER_TOKEN")
    else:
        token = getenv("K8S_QA_EXTERNAL_API_BEARER_TOKEN")

    heads = {
        'Authorization': f'Bearer {token}',
    }

    # for i in range(0, 1):
        # recipe = {
        #     "table_name": "5_5bb461c9-4f12-4fd9-81b3-0faf590c1da5_photos",
        # }
        # request_with_body_and_photo(url, recipe, "post", heads, "test_images/small/test_image.jpg")
        # request_with_body_and_photo(url, recipe, "post", heads, "test_images/small/test_image.jpg")

    # directory = 'test_images/small_with_face'
    # directory = 'test_images/small_selection'
    directory = 'test_images/small'
    # directory = 'test_images/similarity'
    # directory = 'test_images/all_same'
    # directory = 'test_images/all_same_smaller'

    for filename in listdir(directory):
        ext = path.splitext(filename)[1]
        if ext.lower() == '.jpg':
            file_path = path.join(directory, filename)
            logger.info(f"file path is: {file_path}")
            request_with_body_and_photo(url, recipe, "post", heads, file_path)

    # get token
    # request_with_body(url, token_body, "post", heads)
