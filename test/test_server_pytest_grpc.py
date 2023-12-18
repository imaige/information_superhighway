# import pytest
# import mock
# import grpc
#
# from proto_models.internal_api_template_service_pb2 import TemplateRequest, TemplateReply
#
#
# @pytest.fixture(scope='module')
# def grpc_add_to_server():
#     from proto_models.internal_api_template_service_pb2_grpc import add_InternalApiTemplateServiceServicer_to_server
#     return add_InternalApiTemplateServiceServicer_to_server
#
#
# @pytest.fixture(scope='module')
# def grpc_servicer():
#     from app.app.internal_api_template_service_server.internal_api_template_service_server import TemplateRequester
#     return TemplateRequester()
#
#
# @pytest.fixture(scope='module')
# def grpc_stub_cls(grpc_channel):
#     from proto_models.internal_api_template_service_pb2_grpc import InternalApiTemplateServiceStub
#     return InternalApiTemplateServiceStub
#
#
# @pytest.mark.asyncio
# async def test_request(grpc_stub):
#     request = TemplateRequest(name="Test")
#     mock_context = mock.create_autospec(spec=grpc.aio.ServicerContext)
#     response = await grpc_servicer().InternalApiTemplateRequest(request, mock_context)
#     result = [x for x in response]
#     assert result == [TemplateReply(message="Hello, Test!")]
