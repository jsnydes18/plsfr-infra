import os
from aws_cdk import (
    aws_lambda as _lambda,
)

def pull_lambda(self):
    handler_path = os.path.dirname(os.path.realpath(__file__))
    function = _lambda.Function(self, "RequestPullFunction",
        runtime=_lambda.Runtime.NODEJS_18_X,
        handler="request/pull.handler",
        code=_lambda.Code.from_asset(os.path.join(handler_path, "../handlers/handlers.zip"))
    )
    return function

def submit_lambda(self):
    handler_path = os.path.dirname(os.path.realpath(__file__))
    function = _lambda.Function(self, "RequestSubmitFunction",
        runtime=_lambda.Runtime.NODEJS_18_X,
        handler="request/submit.handler",
        code=_lambda.Code.from_asset(os.path.join(handler_path, "../handlers/handlers.zip"))
    )
    return function