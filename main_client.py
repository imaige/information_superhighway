from app.src.internal_api_template_service_orchestrator_client import internal_api_template_service_orchestrator_client
import asyncio
import sys


def main():
    print("path: ", sys.path)
    print("Running main client script.")
    asyncio.run(internal_api_template_service_orchestrator_client.run())


if __name__ == "__main__":
    main()
