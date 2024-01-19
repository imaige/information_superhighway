from src.app.internal_api_template_service_orchestrator_client import internal_api_template_service_orchestrator_client
import asyncio
from src.libraries.logging_file_format import configure_logger
import logging
from proto_models.internal_api_template_service_pb2 import (
    ImageRequest, ImageReply, TemplateRequest, TemplateReply
)
import sys


async def main():
    logger = logging.getLogger(__name__)
    configure_logger(logger, level=logging.INFO)
    logger.info("Running main client script.")

    if len(sys.argv) != 3:
        print("Usage: python script.py <request_destination>")
        sys.exit(1)

    # await internal_api_template_service_orchestrator_client.run(
    #     "template_request",
    #     TemplateRequest(name="caleb"))
    await internal_api_template_service_orchestrator_client.run(
        # "template_image_request",
        sys.argv[1],
        TemplateRequest(name="caleb"),
        sys.argv[2]
    )


if __name__ == "__main__":
    asyncio.run(main())
