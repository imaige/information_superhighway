import grpc
import grpc_testing
import pytest

from proto_models import internal_api_template_service_pb2
from proto_models import internal_api_template_service_pb2_grpc
from src.app.internal_api_template_service_server.internal_api_template_service_server import TemplateRequester


class TestTemplateRpc:
    def setUp(self):
        # add all servers/servicers to this list
        # syntax: [protobuf file].DESCRIPTOR.services_by_name['ServiceName']: [ServerOrServicerClass()]
        # you can find each ServiceName by looking at the .proto file for the service you would like to test
        # anything defined using 'service $RandomService { }' should be tested
        servicers = {
            internal_api_template_service_pb2.DESCRIPTOR.services_by_name['InternalApiTemplateService']:
                TemplateRequester()
        }

        self.test_server = grpc_testing.server_from_dictionary(
            servicers, grpc_testing.strict_real_time())

    @pytest.mark.asyncio
    async def test_templaterequest(self):
        self.setUp()
        """ expect to get TemplateRequest response with the provided name """
        name = "John Doe"
        request = internal_api_template_service_pb2.TemplateRequest(name=name)

        print("services is:")
        for service in internal_api_template_service_pb2.DESCRIPTOR.services_by_name:
            print("service is: "+service)
            for method in internal_api_template_service_pb2.DESCRIPTOR.services_by_name[service].methods_by_name:
                print("method is: "+method)

        # you can find each Method by looking at the .proto file for the service you would like to test
        # for each service, anything defined using 'rpc $RandomEndpoint($RandomRequest) returns ($RandomReply);' should
        # be tested
        templaterequest_method = self.test_server.invoke_unary_unary(
            method_descriptor=(internal_api_template_service_pb2.DESCRIPTOR
                .services_by_name['InternalApiTemplateService']
                .methods_by_name['InternalApiTemplateRequest']),
            invocation_metadata={},
            request=request, timeout=1)

        # run template rpc request
        response_async, metadata, code, details = templaterequest_method.termination()

        # unwrap async list of responses
        response = [i async for i in response_async]

        assert response[0].message == f'Hello, {name}!'
        assert code == grpc.StatusCode.OK


if __name__ == '__main__':
    pytest.main()
