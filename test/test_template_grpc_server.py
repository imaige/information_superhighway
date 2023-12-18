import grpc
import grpc_testing
import pytest

from proto_models import internal_api_template_service_pb2
from proto_models import internal_api_template_service_pb2_grpc
from src.app.internal_api_template_service_server.internal_api_template_service_server import TemplateRequester


class TestGreeter:
    def setUp(self):
        servicers = {
            internal_api_template_service_pb2.DESCRIPTOR.services_by_name['InternalApiTemplateService']:
                TemplateRequester()
        }

        self.test_server = grpc_testing.server_from_dictionary(
            servicers, grpc_testing.strict_real_time())

    @pytest.mark.asyncio
    async def test_templaterequest(self):
        self.setUp()
        """ expect to get Greeter response """
        name = "John Doe"
        request = internal_api_template_service_pb2.TemplateRequest(name=name)
        print("descriptor is: ")
        print(internal_api_template_service_pb2.DESCRIPTOR)
        print("services is:")
        for service in internal_api_template_service_pb2.DESCRIPTOR.services_by_name:
            print("service is: "+service)
            for method in internal_api_template_service_pb2.DESCRIPTOR.services_by_name[service].methods_by_name:
                print("method is: "+method)

        templaterequest_method = self.test_server.invoke_unary_unary(
            method_descriptor=(internal_api_template_service_pb2.DESCRIPTOR
                .services_by_name['InternalApiTemplateService']
                .methods_by_name['InternalApiTemplateRequest']),
            invocation_metadata={},
            request=request, timeout=1)

        response_async, metadata, code, details = templaterequest_method.termination()
        response = [i async for i in response_async]
        print("output is:")
        print("response: ", response)
        print("code: ", code)
        print("details: ", details)
        assert response[0].message == f'Hello, {name}!'
        assert code == grpc.StatusCode.OK


if __name__ == '__main__':
    pytest.main()
