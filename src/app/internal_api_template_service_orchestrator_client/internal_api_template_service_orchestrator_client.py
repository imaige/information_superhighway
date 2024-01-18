from ...libraries.logging_file_format import configure_logger
from .template_basic_request import template_request
from .template_image_request import template_image_request
from proto_models.internal_api_template_service_pb2 import (
    ImageRequest, ImageReply, TemplateRequest, TemplateReply
)

import asyncio
import logging
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Check env
APP_ENV = getenv("IMAIGE_PYTHON_APP_ENVIRONMENT")
match APP_ENV:
    case "LOCAL":
        load_dotenv(".env.local")

logger = logging.getLogger(__name__)
configure_logger(logger, level=logging.INFO)


async def run(func_name: str, request_obj: any, request_destination: str):
    match func_name:
        case "template_request":
            logger.info(f'Orchestrator making template basic request to port {getenv("GRPC_ACCESS_PORT")}')
            await template_request(request_obj, getenv("GRPC_ACCESS_PORT").strip())
        case "template_image_request":
            logger.info(f'Orchestrator making template image request to port {getenv("GRPC_ACCESS_PORT")}')
            # await template_image_request(None, getenv("GRPC_ACCESS_PORT").strip())
            await template_image_request(None, request_destination.strip())



if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(template_request(TemplateRequest(name="caleb"), getenv("GRPC_ACCESS_PORT")))
