#!/usr/bin/env python3
import aws_cdk as cdk

from plsfr.plsfr_stack import PlsfrStack

app = cdk.App()
PlsfrStack(app, "PlsfrStack",
    env=cdk.Environment(account="677532242987", region="us-east-2"), # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
)

app.synth()
