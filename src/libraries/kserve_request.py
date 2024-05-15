import io

from kserve import InferRequest, InferInput, InferenceServerClient
import json
import base64
import os
import time
import grpc
from proto_models.image_comparison_outputs_pb2 import ImageComparisonOutput, StatusResponse
from proto_models.image_comparison_outputs_pb2_grpc import ImageComparisonOutputServiceStub
from src.libraries.logging_file_format import configure_logger
from src.libraries.get_tls_certs import get_secret_data, get_secret_files

import asyncio
import logging


logger = logging.getLogger(__name__)
configure_logger(logger, level=logging.INFO)


#TODO: add auth to gRPC server as well as to this below client
# of note, kserve as of now does not support secure gRPC requests
# may be worth making an open source contribution to enable secure servers
# see line 61 of this file (as of 2/22/24):
# https://github.com/kserve/kserve/blob/99ac7b2050fafb14b7114b94ad6e3fd7ecfe3d15/python/kserve/kserve/protocol/grpc/server.py#L61
# the server class we use - ModelServer - has this as a dependency on line 131 (as of 2/22/24):
# https://github.com/kserve/kserve/blob/99ac7b2050fafb14b7114b94ad6e3fd7ecfe3d15/python/kserve/kserve/model_server.py#L86
async def image_comparison_request(port, b64image: str, model_name: str, request_location: str = None):
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

    client = InferenceServerClient(url=os.environ.get("INGRESS_PORT", port),
                                   ssl=True,
                                   # root_certificates=ca_cert,
                                   # private_key=client_key,
                                   # certificate_chain=client_cert,
                                   creds=creds,
                                   channel_args=(
                                   # grpc.ssl_target_name_override must be set to match CN used in cert gen
                                   ('grpc.ssl_target_name_override', 'ac5ba39f7cbdb40ffb2e8b2e1c9672cd-1882491926.us-east-2.elb.amazonaws.com'),)
                                   )
    # json_file = open("./input.json") #Example image provided in kserving documentation
    # json_file = open("./input_9jpg.json") #Test image of dog, 9x8
    # json_file = open("test_image.json")  # Test image of dog, 64x56
    #
    # data = json.load(json_file)
    infer_input = InferInput(
        name="input-0", shape=[1], datatype="BYTES", data=[base64.b64decode(b64image)]
    )
    request = InferRequest(infer_inputs=[infer_input], model_name="custom-model")

    t0 = time.time()
    for i in range(1):
        # make inference request via gRPC
        logger.info(f"making infer_request request to port {port}")
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
        logger.info(f"received response: {res}")
        for output in res.outputs:
            shape = output.shape[0]
            contents = []
            for j in range(0, shape):
                byte_string = output.contents.bytes_contents[j]
                contents.extend([byte_string])

            grpc_output = ImageComparisonOutput(
                model_name=res.model_name,
                id=res.id,
                name=output.name,
                datatype=output.datatype,
                shape=shape,
                contents=contents
            )

            return grpc_output
