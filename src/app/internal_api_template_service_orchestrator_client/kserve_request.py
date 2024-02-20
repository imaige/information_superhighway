from kserve import InferRequest, InferInput, InferenceServerClient
import json
import base64
import os
import time
import grpc
from proto_models.image_comparison_outputs_pb2 import ImageComparisonOutput, StatusResponse
from proto_models.image_comparison_outputs_pb2_grpc import ImageComparisonOutputServiceStub
from ...libraries.logging_file_format import configure_logger

import asyncio
import logging


logger = logging.getLogger(__name__)
configure_logger(logger, level=logging.INFO)

#TODO: add auth to gRPC server as well as to this below client
async def image_comparison_request(port, b64image: str, model_name: str) -> None:
    client = InferenceServerClient(url=os.environ.get("INGRESS_HOST", "localhost")+":"+os.environ.get("INGRESS_PORT", port),
                                   channel_args=(('grpc.ssl_target_name_override', os.environ.get("SERVICE_HOSTNAME", "")),))
    # json_file = open("./input.json") #Example image provided in kserving documentation
    # json_file = open("./input_9jpg.json") #Test image of dog, 9x8
    json_file = open("test_image.json")  # Test image of dog, 64x56

    data = json.load(json_file)
    infer_input = InferInput(
        name="input-0", shape=[1], datatype="BYTES", data=[base64.b64decode(b64image)]
    )
    request = InferRequest(infer_inputs=[infer_input], model_name=model_name)

    t0 = time.time()
    for i in range(1):
        # make inference request via gRPC
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
            logger.info(f"grpc_output is: {grpc_output} and is of type {type(grpc_output)}")

            # async with grpc.aio.insecure_channel(port) as channel:
            #     stub = ImageComparisonOutputServiceStub(channel)
            #     logger.info(f"making request to {port}")
            #     async for response in stub.ImageComparisonOutputRequest(grpc_output):
            #         logger.info("Received response: ")
            #         logger.info(response)

