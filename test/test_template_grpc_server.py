import grpc
import grpc_testing
import pytest

from proto_models import internal_api_template_service_pb2
from proto_models import internal_api_template_service_pb2_grpc
from src.app.internal_api_template_service_server.internal_api_template_service_server import TemplateRequester
from src.libraries.grpc_status_code_mapping import numeric_status_code_mapping


# Notably, one thing this test package does not test is varied input types.  This is handled by the protocol buffer, #
# which does not permit input of any data type other than the prescribed one.  E.g. if trying to initialize a #
# TemplateRequest with parameter name=3 or name=["John", "Jim"], it will throw a TypeError. #
class TestTemplateRpc:
    def setUp(self):
        # add all servers/servicers to this list
        # syntax: [$protobuf_file].DESCRIPTOR.services_by_name['$ServiceName']: [$ServerOrServicerClass()]
        # you can find each ServiceName by looking at the .proto file for the service you would like to test
        # anything defined using 'service $RandomService { }' should be tested
        servicers = {
            internal_api_template_service_pb2.DESCRIPTOR.services_by_name['InternalApiTemplateService']:
                TemplateRequester()
        }

        self.test_server = grpc_testing.server_from_dictionary(
            servicers, grpc_testing.strict_real_time())

    @pytest.mark.asyncio
    async def test_templaterequest_name(self):
        self.setUp()
        """ expect to get TemplateRequest response with the provided name """
        name = "John Doe"
        request = internal_api_template_service_pb2.TemplateRequest(name=name)

        # Leaving these statements commented out in case future devs need to log out list of services & methods
        # print("services is:")
        # for service in internal_api_template_service_pb2.DESCRIPTOR.services_by_name:
        #     print("service is: "+service)
        #     for method in internal_api_template_service_pb2.DESCRIPTOR.services_by_name[service].methods_by_name:
        #         print("method is: "+method)

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

    @pytest.mark.asyncio
    async def test_templaterequest_invalid_proto(self):
        self.setUp()
        """ expect to get INVALID_ARGUMENT error """
        name = "John Doe"

        class FailedRequest:
            def __init__(self, not_name):
                self.name = not_name

        request = FailedRequest(name)

        templaterequest_method = self.test_server.invoke_unary_unary(
            method_descriptor=(internal_api_template_service_pb2.DESCRIPTOR
            .services_by_name['InternalApiTemplateService']
            .methods_by_name['InternalApiTemplateRequest']),
            invocation_metadata={},
            request=request, timeout=1)

        # run template rpc request
        response_async, metadata, code, details = templaterequest_method.termination()
        # assert code == grpc.StatusCode.INVALID_ARGUMENT

        # unwrap async list of responses
        response = [i async for i in response_async]
        print("response is: ", response, "which has type ", type(response))

        status_code = numeric_status_code_mapping[response[0].code]
        assert status_code == grpc.StatusCode.INVALID_ARGUMENT, f"Expected INVALID_ARGUMENT, but got {status_code}"
        assert ('Invalid argument error'
                in response[0].message), f"Expected AttributeError, but got: {response[0].message}"
        details_value_str = response[0].details[0].value.decode('utf-8')
        assert ('Invalid argument: request must use TemplateRequest protocol buffer.'
                in details_value_str), f"Expected predefined message, but got: {details_value_str}"

    @pytest.mark.asyncio
    async def test_templaterequest_empty_name(self):
        self.setUp()
        """ expect to get TemplateRequest response with the provided name, which is an empty string """
        name = ""
        request = internal_api_template_service_pb2.TemplateRequest(name=name)
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

    @pytest.mark.asyncio
    async def test_templaterequest_numeric_string_name(self):
        self.setUp()
        """ expect to get TemplateRequest response with the provided name, which is numeric but in string form """
        name = "3478239479327489237489327489237489327483297489237489273412312309871"
        request = internal_api_template_service_pb2.TemplateRequest(name=name)
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
