from src.app.internal_api_template_service_orchestrator_client import internal_api_template_service_orchestrator_client
import asyncio
from src.libraries.logging_file_format import configure_logger, get_log_level
import logging
from proto_models.internal_api_template_service_pb2 import (
    ImageRequest, ImageReply, TemplateRequest, TemplateReply
)
from proto_models.analysis_layer_pb2 import AiModelOutputRequest
import sys


async def main():
    logger = logging.getLogger(__name__)
    log_level = get_log_level()
    configure_logger(logger, level=log_level)
    logger.info("Running main client script.")

    if len(sys.argv) != 3:
        print("Usage: python script.py <function_name> <request_destination>")
        sys.exit(1)

    # await internal_api_template_service_orchestrator_client.run(
    #     "template_request",
    #     TemplateRequest(name="caleb"))
    await internal_api_template_service_orchestrator_client.run(
        # "template_image_request",
        sys.argv[1],
        # TemplateRequest(name="caleb"),
        AiModelOutputRequest(
            photo_id=1,
            image_comparison_run_id="run-id-test",
            image_comparison_name="img-comparison-name",
            image_comparison_datatype="test-datatype",
            image_comparison_shape=3,
            image_comparison_contents=["test1".encode(), "test2".encode()]
        ),
        sys.argv[2]
    )


if __name__ == "__main__":
    asyncio.run(main())
