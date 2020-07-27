#!/usr/bin/env python3
import os

from aws_cdk import core

from lib.login import Login

app = core.App()

env = {"region": "eu-west-1"}

domain_name = os.getenv("DOMAIN_NAME")
if domain_name is None:
    raise RuntimeError("Please set the DOMAIN_NAME environment variable")


Login(app, "login", domain_name, env=env)

app.synth()
