import requests
from typing import Dict, Union, List
import logging

from requests import JSONDecodeError

from logging_file_format import configure_logger
import json
from os import getenv, path, listdir
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
configure_logger(logger, level=logging.INFO)

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
    recipe = {
        "name": "test-recipe",
        "description": "describe me",
        "models": [
            "image_comparison_hash_model",
            "colors_basic_model",
            "image_classification_model",
            "face_detect_model",
            # "image_classification_model"
        ]
    }
    token = getenv("K8S_EXTERNAL_API_BEARER_TOKEN")

    token_body = {
        "name": "Test1 User1",
        "email": "test1@example.com",
        "password": "Password1!",
        "profile_picture": "test1.jpg",
        "account_type": 1,
        "company_id": 1
    }

    heads = {
        'Authorization': f'Bearer {token}',
    }

    # local photo ai request
    # url = "http://0.0.0.0:8000/api/v1/photos/model_request"
    # local vanilla photo create
    # url = "http://0.0.0.0:8000/api/v1/photos/"

    # k8s vanilla photo create
    # url = "http://acb5bb47a60054e3ab8f6f2bab81a51c-1018561966.us-east-2.elb.amazonaws.com:80/api/v1/photos/"
    # k8s photo ai request
    url = "https://api.mediaviz.ai/api/v1/photos/model_request"

    # token
    # url = "http://acb5bb47a60054e3ab8f6f2bab81a51c-1018561966.us-east-2.elb.amazonaws.com:80/api/v1/token"

    for i in range(0, 25):
        request_with_body_and_photo(url, recipe, "post", heads, "test_image.jpg")

    directory = 'test_images/small_selection'

    for filename in listdir(directory):
        ext = path.splitext(filename)[1]
        if ext.lower() == '.jpg':
            file_path = path.join(directory, filename)
            # logger.info(f"file path is: {file_path}")
            # request_with_body_and_photo(url, recipe, "post", heads, file_path)

    # get token
    # request_with_body(url, token_body, "post", heads)
