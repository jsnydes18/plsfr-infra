import boto3
import uuid
import random
import string
import pdb

endpoint_url = "http://localhost.localstack.cloud:4566"
dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)
table = dynamodb.Table('pullTable')

for x in range(1,5):
    msgId = str(uuid.uuid4())
    pages = random.randint(1,10)
    for y in range(1,pages):
        item = {
                'reqId': msgId,
                'pageNum': str(y),
                'results': random.choices(string.ascii_letters + string.digits, k=16),
            }
        print(item)
        table.put_item(
            Item=item
        )