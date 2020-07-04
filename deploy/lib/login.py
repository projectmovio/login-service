from aws_cdk import core
from aws_cdk.aws_cognito import UserPool


class Login(core.Stack):

    def __init__(self, app: core.App, id: str, **kwargs) -> None:
        super().__init__(app, id, **kwargs)
        self._create_userpool()

    def _create_userpool(self):
        UserPool(
            self,
            "movio",
            user_pool_name="movio-userpool"
        )
