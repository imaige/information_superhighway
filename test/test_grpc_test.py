import grpc
import grpc_testing
import pytest

from proto_models import internal_api_template_service_pb2
from proto_models import internal_api_template_service_pb2_grpc
from src.app.internal_api_template_service_server.internal_api_template_service_server import TemplateRequester


class TestGreeter:
    def setUp(self):
        servicers = {
            internal_api_template_service_pb2_grpc.InternalApiTemplateServiceServicer: TemplateRequester()
        }

        self.test_server = grpc_testing.server_from_dictionary(
            servicers, grpc_testing.strict_real_time())

    def test_helloworld(self):
        self.setUp()
        """ expect to get Greeter response """
        name = "John Doe"
        request = internal_api_template_service_pb2.TemplateRequest(name=name)

        sayhello_method = self.test_server.invoke_unary_stream(
            method_descriptor=(internal_api_template_service_pb2.DESCRIPTOR
                .services_by_name['']
                .TemplateRequest),
            invocation_metadata={},
            request=request, timeout=1)

        response, metadata, code, details = sayhello_method.termination()
        self.assertEqual(response.message, f'Hello, {name}!')
        self.assertEqual(code, grpc.StatusCode.OK)


if __name__ == '__main__':
    unittest.main()
