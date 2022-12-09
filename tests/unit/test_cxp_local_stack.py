import aws_cdk as core
import aws_cdk.assertions as assertions

from cxp_local.cxp_local_stack import CxpLocalStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cxp_local/cxp_local_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CxpLocalStack(app, "cxp-local")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
