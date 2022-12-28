from aws_cdk import (
    Duration,
    aws_sqs as sqs,
    aws_dynamodb as ddb
)

def create_queue(self):
    queue_name = 'submitq'
    queue = sqs.Queue(
        self, queue_name,
        queue_name=queue_name,
        visibility_timeout=Duration.seconds(5),
    )
    queue.grant_send_messages(self.node.find_child("RequestSubmitFunction"))
    return queue

def create_table(self):
    # Request Results Collection Table
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
    table.grant_read_data(self.node.find_child("RequestPullFunction"))
    return table
