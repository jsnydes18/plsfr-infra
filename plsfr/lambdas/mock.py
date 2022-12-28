import os
from aws_cdk import (
    aws_lambda as _lambda,
)

def pull_lambda(self):
    handler_path = os.path.dirname(os.path.realpath(__file__))
    function = _lambda.Function(self, "MockPullFunction",
        runtime=_lambda.Runtime.NODEJS_18_X,
        handler="mock/pull.handler",
        code=_lambda.Code.from_asset(os.path.join(handler_path, "../handlers/handlers.zip"))
    )
    return function

def submit_lambda(self):
    handler_path = os.path.dirname(os.path.realpath(__file__))
    function = _lambda.Function(self, "MockSubmitFunction",
        runtime=_lambda.Runtime.NODEJS_18_X,
        handler="mock/submit.handler",
        code=_lambda.Code.from_asset(os.path.join(handler_path, "../handlers/handlers.zip"))
    )
    return function