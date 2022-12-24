from aws_cdk import (
    Stack
)
from constructs import Construct
from plsfr import (
    decouplers,
    apigw
)

class PlsfrStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        table = decouplers.create_table(self)
        queue = decouplers.create_queue(self)
        api = apigw.create_api(self)