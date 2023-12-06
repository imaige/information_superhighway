from app.src.internal_api_template_service_service import internal_api_template_service_service, internal_api_template_service_service_test
import asyncio


def main():
    asyncio.run(internal_api_template_service_service_test.serve())


if __name__ == "__main__":
    main()
