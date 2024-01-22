to run server:
- python main.py

to run client:
- python main_client.py <function_name> <request_destination>

to test:
- python test.py

to build with Docker:
- docker build -t internal_api_template_service .
- from root
- note that this will take a long time (3-4 minutes common).  packing of gRPC Python utilities (grpcio, grpcio-tools) is the culprit.

to run with Docker:
- docker run -p [port]:[port] internal_api_template_service
- environment variable GRPC_SERVER_PORT must start with 0.0.0.0 to bind all addresses at the desired port
