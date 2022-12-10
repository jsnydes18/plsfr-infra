from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_dynamodb as ddb
)
from constructs import Construct

class CxpLocalStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        queue_name = 'submitq'
        queue = sqs.Queue(
            self, queue_name,
            queue_name=queue_name,
            visibility_timeout=Duration.seconds(5),
        )

        ddb_table_name = "pullTable"
        partition_key = "msgId"
        sort_key = "pageNum"
        ttl_key = "ttl"
        table = ddb.Table(
            self, ddb_table_name,
            table_name=ddb_table_name,
            partition_key=ddb.Attribute(name=partition_key, type=ddb.AttributeType.STRING),
            sort_key=ddb.Attribute(name=sort_key, type=ddb.AttributeType.STRING),
            time_to_live_attribute=ttl_key, #  Unix epoch time format in second
            billing_mode=ddb.BillingMode.PROVISIONED,
            write_capacity=20,
            read_capacity=20
        )
