from proto_models.internal_api_template_service_pb2 import (
    TemplateRequest, TemplateReply, ImageRequest, ImageReply
)
from proto_models.internal_api_template_service_pb2_grpc import (
    InternalApiTemplateServiceServicer, add_InternalApiTemplateServiceServicer_to_server
)
from proto_models.image_comparison_outputs_pb2 import (
    ImageComparisonOutput, StatusResponse
)
from proto_models.image_comparison_outputs_pb2_grpc import (
    ImageComparisonOutputServiceServicer, add_ImageComparisonOutputServiceServicer_to_server
)
from proto_models.information_superhighway_pb2 import (
    ImageAnalysisRequest
)
from proto_models.information_superhighway_pb2_grpc import (
    InformationSuperhighwayServiceServicer, add_InformationSuperhighwayServiceServicer_to_server
)
from src.libraries import kserve_request
from ...libraries.grpc_server_factory import create_secure_server
from ...libraries.logging_file_format import configure_logger
import logging

import grpc
import asyncio
from google.rpc import status_pb2, code_pb2, error_details_pb2
from google.protobuf import any_pb2

import base64
from PIL import Image, ImageOps
from io import BytesIO

from os import getenv
from dotenv import load_dotenv

from typing import Union

load_dotenv()

# Check env
APP_ENV = getenv("IMAIGE_PYTHON_APP_ENVIRONMENT")
if APP_ENV == "LOCAL":
    load_dotenv(".env.local")

logger = logging.getLogger(__name__)
configure_logger(logger, level=logging.INFO)


# Service Class Definition #
class TemplateRequester(InternalApiTemplateServiceServicer):
    # Endpoint definition #
    # Matches name in InternalApiTemplateServiceServicer
    async def InternalApiTemplateRequest(
            self, request: TemplateRequest, context: grpc.ServicerContext
    ) -> Union[TemplateReply, status_pb2.Status]:
        logger.info(f"Serving basic request with detail: {request}")
        # Example error handling
        # in this case, for using a protocol buffer that is not the designated one
        # IMO, Python does not enforce the 'same protocol buffer' requirement as stringently as it should
        # so it would be good practice to enforce this on our end using simple logic like the below
        # Note - all fields in gRPC protocol buffers are optional, which we can take advantage of to pass as little
        # information as possible; as such, the following type checking is (probably) excessive, but helpful as an
        # illustrative example of error handling
        if not isinstance(request, TemplateRequest):
            logger.info(f"Failure in method call")
            code = code_pb2.INVALID_ARGUMENT
            details = any_pb2.Any()
            # to access details for a particular error, use response[$index].details[0].value.decode('utf-8')
            # as details is passed as a list and the value parameter is passed as a protobuf-serialized string
            details.Pack(
                error_details_pb2.DebugInfo(
                    detail="Invalid argument: request must use TemplateRequest protocol buffer."
                )
            )
            message = "Invalid argument error."
            yield status_pb2.Status(
                code=code,
                message=message,
                details=[details]
            )
        # send response (optional, but recommended)
        yield TemplateReply(message=f"Hello, {request.name}!")

    async def InternalApiTemplateImageRequest(
      self, request: ImageRequest, context: grpc.aio.ServicerContext
    ) -> ImageReply:
        if not isinstance(request, ImageRequest):
            logger.info(f"Failure in photo request call")
            code = code_pb2.INVALID_ARGUMENT
            details = any_pb2.Any()
            # to access details for a particular error, use response[$index].details[0].value.decode('utf-8')
            # as details is passed as a list and the value parameter is passed as a protobuf-serialized string
            details.Pack(
                error_details_pb2.DebugInfo(
                    detail="Invalid argument: request must use ImageRequest protocol buffer."
                )
            )
            message = "Invalid argument error."
            yield status_pb2.Status(
                code=code,
                message=message,
                details=[details]
            )
        logger.info(f"Serving photo request with detail: {request}")

        # get image from request, decode from b64, cast to BytesIO, open
        decoded_image = Image.open(BytesIO(base64.b64decode(request.b64image)))

        # optionally, do something with the image, including but not limited to:
        # modify color, scale down, crop, send request to other server
        converted_image = ImageOps.grayscale(decoded_image)

        image_stream = BytesIO()

        decoded_image.save(image_stream, format="PNG")
        # converted_image.save(image_stream, format="PNG")

        bytes_image = image_stream.getvalue()
        response_image = base64.b64encode(bytes_image)
        yield ImageReply(b64image=response_image)


class ImageComparisonOutputRequester(ImageComparisonOutputServiceServicer):
    # Endpoint definition #
    # Matches name in ImageComparisonOutputServiceServicer
    async def ImageComparisonOutputRequest(
        self, request: ImageComparisonOutput, context: grpc.aio.ServicerContext
    ) -> StatusResponse:
        logger.info(f"Serving image comparison output request with detail: {request}")

        logger.info(f"Request model name is: {request.model_name}")
        logger.info(f"Request contents is: {request.contents}")

        yield StatusResponse(message="OK")


class InformationSuperhighway(InformationSuperhighwayServiceServicer):
    # Endpoint definition #
    # Matches name in InformationSuperhighwayServiceServicer
    async def ImageAiAnalysisRequest(
        self, request: ImageAnalysisRequest, context: grpc.aio.ServicerContext
    ) -> StatusResponse:
        logger.info(f"Serving image comparison output request with model name: {request.model_name}")
        # logger.info(f"and detail: {request.b64image}")
        request_image = request.b64image
        # convert image: decode to b64, convert to BytesIO, convert to Pillow image using open, optionally show
        # decoded_image = base64.b64decode(request_image)
        # bytes_image = BytesIO(decoded_image)
        # final_image = Image.open(bytes_image)
        # final_image.show()

        if request.model_name == "image_comparison":
            image_comparison_output = await kserve_request.image_comparison_request(
                # 'adea6b821626048b2a3c0032f0f71841-1183079.us-east-2.elb.amazonaws.com:80',
                # '0.0.0.0:8081',
                'ac5ba39f7cbdb40ffb2e8b2e1c9672cd-1882491926.us-east-2.elb.amazonaws.com:80',
                request.b64image, request.model_name, 'k8s_ai_service')
            # TODO: turn output into valid protobuf object (incl. photo id) and send via gRPC to analysis layer

            yield StatusResponse(message="OK")

        elif request.model_name == "color":
            # TODO: implement me, similar to above; do same for other AI models
            pass




# Server Creation #
async def serve() -> None:
    # flow for running locally
    request_location = "k8s_info_superhighway"
    server_key = f'./tls_certs/{request_location}/server-key.pem'
    server_cert = f'./tls_certs/{request_location}/server-cert.pem'
    ca_cert = f'./tls_certs/{request_location}/ca-cert.pem'

    port = getenv("GRPC_SERVER_PORT").strip()
    service_classes = [
        {
            "add_func": add_InternalApiTemplateServiceServicer_to_server,
            "add_class": TemplateRequester()
        },
        {
            "add_func": add_ImageComparisonOutputServiceServicer_to_server,
            "add_class": ImageComparisonOutputRequester()
        },
        {
            "add_func": add_InformationSuperhighwayServiceServicer_to_server,
            "add_class": InformationSuperhighway()
        },
    ]

    server = create_secure_server(port, service_classes, server_key, server_cert, ca_cert)
    # server = create_insecure_server(port, service_classes)

    logger.info("Starting server on %s", port)
    await server.start()
    logger.info(f"Server started. Listening on port {port}...")
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(serve())
