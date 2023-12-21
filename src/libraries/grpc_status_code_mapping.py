from grpc import StatusCode

grpc_status_code_mapping = {
    StatusCode.OK: 0,
    StatusCode.CANCELLED: 1,
    StatusCode.UNKNOWN: 2,
    StatusCode.INVALID_ARGUMENT: 3,
    StatusCode.DEADLINE_EXCEEDED: 4,
    StatusCode.NOT_FOUND: 5,
    StatusCode.ALREADY_EXISTS: 6,
    StatusCode.PERMISSION_DENIED: 7,
    StatusCode.UNAUTHENTICATED: 16,
    StatusCode.RESOURCE_EXHAUSTED: 8,
    StatusCode.FAILED_PRECONDITION: 9,
    StatusCode.ABORTED: 10,
    StatusCode.OUT_OF_RANGE: 11,
    StatusCode.UNIMPLEMENTED: 12,
    StatusCode.INTERNAL: 13,
    StatusCode.UNAVAILABLE: 14,
    StatusCode.DATA_LOSS: 15,
}

# Reverse mapping for integer to gRPC status code
numeric_status_code_mapping = {v: k for k, v in grpc_status_code_mapping.items()}
