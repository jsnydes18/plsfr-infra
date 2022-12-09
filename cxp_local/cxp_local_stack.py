from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
)
from constructs import Construct

class CxpLocalStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        queueName = 'submitq'
        queue = sqs.Queue(
            self, queueName,
            queue_name=queueName,
            visibility_timeout=Duration.seconds(5),
        )
