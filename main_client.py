from app.src.internal_api_template_service_orchestrator_client import internal_api_template_service_orchestrator_client
import asyncio
from app.libraries.logging_file_format import configure_logger
import logging


def main():
    # logging.basicConfig(level=logging.INFO)
    # logging.info("Running main client script.")
    logger = logging.getLogger(__name__)
    configure_logger(logger, level=logging.INFO)
    logger.info("Running main client script.")
    asyncio.run(internal_api_template_service_orchestrator_client.run())


if __name__ == "__main__":
    main()
