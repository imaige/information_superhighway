from src.app.internal_api_template_service_orchestrator_client import internal_api_template_service_orchestrator_client
import asyncio
from src.libraries.logging_file_format import configure_logger
import logging
from proto_models.internal_api_template_service_pb2 import (
    ImageRequest, ImageReply, TemplateRequest, TemplateReply
)


async def main():
    logger = logging.getLogger(__name__)
    configure_logger(logger, level=logging.INFO)
    logger.info("Running main client script.")
    # await internal_api_template_service_orchestrator_client.run(
    #     "template_request",
    #     TemplateRequest(name="caleb"))
    await internal_api_template_service_orchestrator_client.run(
        "template_image_request",
        None)


if __name__ == "__main__":
    asyncio.run(main())
