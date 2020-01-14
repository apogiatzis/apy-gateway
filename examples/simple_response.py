from apy_gateway.api import ApiTemplate

myapi = ApiTemplate()

@myapi.description("My description")
@myapi.name("func_name")
@myapi.function.memory(128)
@myapi.function.role("role_name")
@myapi.function.custom("Timeout", 10)
def ping(event,context):
    return {
        'body': 'Hello there {0}'.format(event['requestContext']['identity']['sourceIp']),
        'headers': {
        'Content-Type': 'text/plain'
        },
        'statusCode': 200
    }