from aws_cdk import (
    aws_apigateway as apigateway,
    aws_iam as iam
)
from plsfr import lambdas, keys

def create_api(self):
    policy = iam.PolicyDocument(
        statements = [
            iam.PolicyStatement(
                actions=["execute-api:Invoke"],
                resources=["execute-api:/prod/*"],
                principals=[
                    iam.ArnPrincipal("arn:aws:iam::677532242987:root"),
                    iam.ArnPrincipal("arn:aws:iam::677532242987:user/Vyn")
                    # iam.AnyPrincipal()
                ]
            )
        ],
    )
    apigw_api_name = "plsfr-api"
    apigw_api = apigateway.RestApi(self, apigw_api_name,
        api_key_source_type=apigateway.ApiKeySourceType.HEADER,
        description="Playlist Surfer Requet Submission and Results Retrieval API",
        disable_execute_api_endpoint=False,
        policy=policy,
        rest_api_name=apigw_api_name,
    )

    key = apigw_api.add_api_key(f"{apigw_api_name}-key",
        api_key_name=f"{apigw_api_name}-key",
        value=keys.PLSFR_API_KEY
    )
    plan = apigw_api.add_usage_plan(f"{apigw_api_name}-usagePlan",
        name="Easy",
        throttle=apigateway.ThrottleSettings(
            rate_limit=10,
            burst_limit=2
        )
    )
    plan.add_api_key(key)

    add_handlers(self, apigw_api)


def add_handlers(self, api):
    # /submit Handler
    submit_api = "submit"
    submit_items = api.root.add_resource(submit_api)
    submit_items.add_method("PUT",
        apigateway.LambdaIntegration(lambdas.submit_lambda(self)),
        api_key_required=True
    )

    # /pull Handler
    pull_api = "pull"
    pull_items = api.root.add_resource(pull_api)
    pull_items.add_method("GET",
        apigateway.LambdaIntegration(lambdas.pull_lambda(self)),
        api_key_required=True
    )