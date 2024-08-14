import io

from kserve import InferRequest, InferInput, InferenceServerClient
import json
import base64
import os
import time
import grpc
from proto_models.image_comparison_outputs_pb2 import ImageComparisonOutput, StatusResponse
from proto_models.image_comparison_outputs_pb2_grpc import ImageComparisonOutputServiceStub
from proto_models.analysis_layer_pb2 import AiModelOutputRequest
from src.libraries.logging_file_format import configure_logger, get_log_level
from src.libraries.get_tls_certs import get_secret_data, get_secret_files

import asyncio
import logging


logger = logging.getLogger(__name__)
log_level = get_log_level()
configure_logger(logger, level=log_level)


#TODO: add auth to gRPC server as well as to this below client
# of note, kserve as of now does not support secure gRPC requests
# may be worth making an open source contribution to enable secure servers
# see line 61 of this file (as of 2/22/24):
# https://github.com/kserve/kserve/blob/99ac7b2050fafb14b7114b94ad6e3fd7ecfe3d15/python/kserve/kserve/protocol/grpc/server.py#L61
# the server class we use - ModelServer - has this as a dependency on line 131 (as of 2/22/24):
# https://github.com/kserve/kserve/blob/99ac7b2050fafb14b7114b94ad6e3fd7ecfe3d15/python/kserve/kserve/model_server.py#L86
async def image_comparison_request(url: str, b64image: str, model_name: str, request_location: str = None):
    # flow for local request
    # client_key = f'./tls_certs/{request_location}/client-key.pem'
    # client_cert = f'./tls_certs/{request_location}/client-cert.pem'
    # ca_cert = f'./tls_certs/{request_location}/ca-cert.pem'

    # flow for request to server running on k8s
    tls_certs = get_secret_data("default", "k8s-image-compare-service-tls-certs")
    client_key = tls_certs.get("client-key")
    client_cert = tls_certs.get("client-cert")
    ca_cert = tls_certs.get("ca-cert")

    creds = grpc.ssl_channel_credentials(
        root_certificates=ca_cert, private_key=client_key, certificate_chain=client_cert
    )

    client = InferenceServerClient(url=url+':80',
                                   ssl=True,
                                   # root_certificates=ca_cert,
                                   # private_key=client_key,
                                   # certificate_chain=client_cert,
                                   creds=creds,
                                   channel_args=(
                                   # grpc.ssl_target_name_override must be set to match CN used in cert gen
                                   ('grpc.ssl_target_name_override', url),)
                                   )
    # json_file = open("./input.json") #Example image provided in kserving documentation
    # json_file = open("./input_9jpg.json") #Test image of dog, 9x8
    # json_file = open("test_image.json")  # Test image of dog, 64x56
    #
    # data = json.load(json_file)
    infer_input = InferInput(
        name="input-0", shape=[1], datatype="BYTES", data=[base64.b64decode(b64image)]
    )
    request = InferRequest(infer_inputs=[infer_input], model_name="image-comparison-model")

    t0 = time.time()
    for i in range(1):
        # make inference request via gRPC
        logger.info(f"making infer request request to image comparison model")
        res = client.infer(infer_request=request)
        '''
        response format:
        model_name: "custom-model"
        id: "5c898bf3-5657-43fa-8969-53a484594541"
        outputs {
            name: "output-0"
            datatype: "BYTES"
            shape: 5
            contents {
                bytes_contents: "fffdbd9dc1c0e7ff"
                bytes_contents: "eb9e93618c9671c8"
                bytes_contents: "36d9292b935f4d93"
                bytes_contents: "fffd9d19c0c021c1"
                bytes_contents: "07e00000000"
            }
        }
        '''
        logger.info(f"received response from kserve image compare request: {res}")

        return res


async def colors_request(url: str, b64image: str, model_name: str, request_location: str = None):
    # flow for request to server running on k8s
    tls_certs = get_secret_data("default", "k8s-colors-model-tls-certs")
    client_key = tls_certs.get("client-key")
    client_cert = tls_certs.get("client-cert")
    ca_cert = tls_certs.get("ca-cert")

    creds = grpc.ssl_channel_credentials(
        root_certificates=ca_cert, private_key=client_key, certificate_chain=client_cert
    )

    client = InferenceServerClient(url=url+':80',
                                   ssl=True,
                                   creds=creds,
                                   channel_args=(
                                       # grpc.ssl_target_name_override must be set to match CN used in cert gen
                                       ('grpc.ssl_target_name_override', url),)
                                   )
    infer_input = InferInput(
        name="input-0", shape=[1], datatype="BYTES", data=[base64.b64decode(b64image)]
    )
    request = InferRequest(infer_inputs=[infer_input], model_name=model_name)

    t0 = time.time()
    for i in range(1):
        # make inference request via gRPC
        logger.info("making infer request to colors model")
        res = client.infer(infer_request=request)
        logger.info(f"received response from kserve colors request: {res}")
        return res


async def face_detect_request(url: str, b64image: str, model_name: str, request_location: str = None):
    # flow for request to server running on k8s
    tls_certs = get_secret_data("default", "k8s-face-detection-model-tls-certs")
    client_key = tls_certs.get("client-key")
    client_cert = tls_certs.get("client-cert")
    ca_cert = tls_certs.get("ca-cert")

    creds = grpc.ssl_channel_credentials(
        root_certificates=ca_cert, private_key=client_key, certificate_chain=client_cert
    )

    client = InferenceServerClient(url=url+':80',
                                   ssl=True,
                                   creds=creds,
                                   channel_args=(
                                       # grpc.ssl_target_name_override must be set to match CN used in cert gen
                                       ('grpc.ssl_target_name_override', url),)
                                   )
    infer_input = InferInput(
        name="input-0", shape=[1], datatype="BYTES", data=[base64.b64decode(b64image)]
    )
    request = InferRequest(infer_inputs=[infer_input], model_name=model_name)

    t0 = time.time()
    for i in range(1):
        # make inference request via gRPC
        logger.info("making infer request to face detection model")
        res = client.infer(infer_request=request)
        # logger.info(f"received response from kserve face detect request: {res}")   # commented this out because raw output was polluting logs
        return res


async def image_classification_request(url: str, b64image: str, model_name: str, request_location: str = None):
    # flow for request to server running on k8s
    tls_certs = get_secret_data("default", "k8s-image-classification-model-tls-certs")
    client_key = tls_certs.get("client-key")
    client_cert = tls_certs.get("client-cert")
    ca_cert = tls_certs.get("ca-cert")

    creds = grpc.ssl_channel_credentials(
        root_certificates=ca_cert, private_key=client_key, certificate_chain=client_cert
    )

    client = InferenceServerClient(url=url+':80',
                                   ssl=True,
                                   creds=creds,
                                   channel_args=(
                                       # grpc.ssl_target_name_override must be set to match CN used in cert gen
                                       ('grpc.ssl_target_name_override', url),)
                                   )
    infer_input = InferInput(
        name="input-0", shape=[1], datatype="BYTES", data=[base64.b64decode(b64image)]
    )
    request = InferRequest(infer_inputs=[infer_input], model_name=model_name)

    t0 = time.time()
    for i in range(1):
        # make inference request via gRPC
        logger.info("making infer request to image classification model")
        res = client.infer(infer_request=request)
        # logger.info(f"received response from kserve face detect request: {res}")   # commented this out because raw output was polluting logs
        return res
