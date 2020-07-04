from aws_cdk import core

import aws_cdk.aws_cognito as cognito


class Login(core.Stack):

    def __init__(self, app: core.App, id: str, **kwargs) -> None:
        super().__init__(app, id, **kwargs)
        self._create_userpool()

    def _create_userpool(self):
        cognito.UserPool(
            self,
            "movio",
            account_recovery=cognito.AccountRecovery.EMAIL_ONLY,
            auto_verify=cognito.AutoVerifiedAttrs(email=True, phone=False),
            mfa=cognito.Mfa.OFF,
            mfa_second_factor=cognito.MfaSecondFactor(otp=True, sms=False),
            self_sign_up_enabled=False,
            sign_in_aliases=cognito.SignInAliases(email=True),
            standard_attributes=cognito.StandardAttributes(
                email=cognito.StandardAttribute(mutable=False, required=True),
            ),
            user_invitation=cognito.UserInvitationConfig(
                email_subject="Movio email verification",
                email_body="Thanks for signing up to movio! Your username is {username} and temporary password is {####}",
            ),
            user_verification=cognito.UserVerificationConfig(
                email_subject="Movio email verification",
                email_body="Thanks for signing up to movio! Verify your account by clicking on {##Verify Email##}",
                email_style=cognito.VerificationEmailStyle.LINK
            ),
        )
