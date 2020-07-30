#!/usr/bin/env python3
import os

from aws_cdk import core

from lib.cert import Cert

app = core.App()

domain_name = "auth.moshan.tv"
cert_stack = Cert(app, "cognito-cert", domain_name, env={"region": "us-east-1"})

app.synth()
