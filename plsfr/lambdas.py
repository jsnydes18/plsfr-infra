import os
from aws_cdk import (
    aws_lambda as _lambda,
    aws_signer as signer,
)

def pull_lambda(self):
    handler_path = os.path.dirname(os.path.realpath(__file__))
    function = _lambda.Function(self, "PullFunction",
        runtime=_lambda.Runtime.NODEJS_18_X,
        handler="pull.handler",
        code=_lambda.Code.from_asset(os.path.join(handler_path, "handlers/pull.mjs.zip"))
    )
    return function

def submit_lambda(self):
    handler_path = os.path.dirname(os.path.realpath(__file__))
    function = _lambda.Function(self, "SubmitFunction",
        runtime=_lambda.Runtime.NODEJS_18_X,
        handler="submit.handler",
        code=_lambda.Code.from_asset(os.path.join(handler_path, "handlers/submit.mjs.zip"))
    )
    return function