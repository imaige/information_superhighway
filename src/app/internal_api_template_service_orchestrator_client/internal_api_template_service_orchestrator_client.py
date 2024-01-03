from ...libraries.logging_file_format import configure_logger
from src.app.internal_api_template_service_orchestrator_client.template_basic_request import template_request
from proto_models.internal_api_template_service_pb2 import (
    ImageRequest, ImageReply, TemplateRequest, TemplateReply
)

import asyncio
import logging
import os
from dotenv import load_dotenv

load_dotenv()

# Check env
APP_ENV = os.getenv("IMAIGE_PYTHON_APP_ENVIRONMENT")
match APP_ENV:
    case "LOCAL":
        load_dotenv(".env.local")

logger = logging.getLogger(__name__)
configure_logger(logger, level=logging.INFO)


async def run(func_name: str, request_obj: any):
    match func_name:
        case "template_request":
            await template_request(request_obj, os.getenv("GRPC_SERVER_PORT"))


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(template_request(TemplateRequest(name="caleb"), os.getenv("GRPC_SERVER_PORT")))
