from app.src.internal_api_template_service_server import internal_api_template_service_server
import asyncio


def main():
    asyncio.run(internal_api_template_service_server.serve())


if __name__ == "__main__":
    main()
