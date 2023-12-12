from app.src.internal_api_template_service_server import internal_api_template_service_server
import asyncio
from app.libraries.logging_file_format import configure_logger
import logging


def main():
    logger = logging.getLogger(__name__)
    configure_logger(logger, level=logging.INFO)
    logger.info("Starting up template service server.")
    asyncio.run(internal_api_template_service_server.serve())


if __name__ == "__main__":
    main()
