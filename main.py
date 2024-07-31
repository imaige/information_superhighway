from src.app.information_superhighway_service_server.information_superhighway_service_server import serve
import asyncio
from src.libraries.logging_file_format import configure_logger
import logging


def main():
    logger = logging.getLogger(__name__)
    configure_logger(logger, level=logging.INFO)
    logger.info("Starting up template service server.")
    asyncio.run(serve())


if __name__ == "__main__":
    main()
