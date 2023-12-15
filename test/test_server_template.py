# import pytest
# from proto_models.internal_api_template_service_pb2 import TemplateRequest, TemplateReply
# from proto_models.internal_api_template_service_pb2_grpc import add_InternalApiTemplateServiceServicer_to_server
# from app.src.internal_api_template_service_server.internal_api_template_service_server import TemplateRequester, serve
#
#
# def test_InternalApiTemplateRequest(mocker):
#     server = mocker.Mock()
#     stub = add_InternalApiTemplateServiceServicer_to_server(TemplateRequester(), server)
#     test_name = "John"
#     request = TemplateRequest(name=test_name)
#
#     response = stub.InternalApiTemplateRequest(request)
#
#     assert response.message == f"Hello, {test_name}!"
# def test_serve(mocker):
#     with mocker.patch('asyncio.run') as mock_run:
#         serve()
#         mock_run.assert_called_once()
#
# if __name__ == '__main__':
#     pytest.main()
