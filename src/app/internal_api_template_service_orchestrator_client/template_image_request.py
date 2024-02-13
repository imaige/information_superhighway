import grpc
from proto_models.internal_api_template_service_pb2 import (
    ImageRequest, ImageReply
)
from proto_models.internal_api_template_service_pb2_grpc import (
    InternalApiTemplateServiceStub
)
from ...libraries.logging_file_format import configure_logger
from ...libraries.get_tls_certs import get_secret_data

import asyncio
import logging
import base64
from PIL import Image
from io import BytesIO

logger = logging.getLogger(__name__)
configure_logger(logger, level=logging.INFO)


async def template_image_request(req: ImageRequest | None, port: str, request_location: str) -> None:
    # flow for running locally
    client_key = open(f'./tls_certs/{request_location}/client-key.pem', 'rb').read()
    client_cert = open(f'./tls_certs/{request_location}/client-cert.pem', 'rb').read()
    ca_cert = open(f'./tls_certs/{request_location}/ca-cert.pem', 'rb').read()

    # flow for running on k8s
    # tls_certs = get_secret_data("default", "tls-certs")
    # client_key = tls_certs.get("client-key")
    # client_cert = tls_certs.get("client-cert")
    # ca_cert = tls_certs.get("ca-cert")

    channel_credentials = grpc.ssl_channel_credentials(
        root_certificates=ca_cert, private_key=client_key, certificate_chain=client_cert
    )

    async with grpc.aio.secure_channel(port, channel_credentials) as channel:
    # async with grpc.aio.insecure_channel(port) as channel:
        stub = InternalApiTemplateServiceStub(channel)
        logger.info(f"Client making InternalApiTemplateImageRequest to port {port}")
        with open('test_image.jpg', 'rb') as file:
            image = file.read()
            encoded_image = base64.b64encode(image)
            async for response in stub.InternalApiTemplateImageRequest(
                ImageRequest(b64image=encoded_image)
            ):
                # get image
                response_image = response.b64image
                # convert image: decode to b64, convert to BytesIO, convert to Pillow image using open, optionally show
                decoded_image = base64.b64decode(response_image)
                bytes_image = BytesIO(decoded_image)
                final_image = Image.open(bytes_image)
                final_image.show()

