from aws_cdk import core
from aws_cdk.aws_cognito import UserPool, Mfa, MfaSecondFactor, UserVerificationConfig, VerificationEmailStyle


class Login(core.Stack):

    def __init__(self, app: core.App, id: str, **kwargs) -> None:
        super().__init__(app, id, **kwargs)
        self._create_userpool()

    def _create_userpool(self):
        UserPool(
            self,
            "movio",
            user_pool_name="movio-userpool",
            mfa=Mfa.OPTIONAL,
            mfa_second_factor=MfaSecondFactor(otp=True, sms=False),
            self_sign_up_enabled=False,
            user_verification=UserVerificationConfig(
                email_subject="Movio email verification",
                email_body="Hello {username}, Thanks for signing up to movio! Verify your account by clicking on {##Verify Email##}",
                email_style=VerificationEmailStyle.LINK
                )
        )
