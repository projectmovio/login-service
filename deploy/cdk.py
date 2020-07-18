#!/usr/bin/env python3
from aws_cdk import core

from lib.login import Login

app = core.App()

env = {"region": "eu-west-1"}

Login(app, "login", env=env)

app.synth()
