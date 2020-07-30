from aws_cdk import core

from aws_cdk.aws_certificatemanager import Certificate, ValidationMethod


class Cert(core.Stack):

    def __init__(self, app: core.App, id: str, domain_name: str, **kwargs) -> None:
        super().__init__(app, id, **kwargs)
        self.domain_name = domain_name
        self._create_cert()

    def _create_cert(self):
        self.cert = Certificate(
            self,
            "certificate",
            domain_name=self.domain_name,
            validation_method=ValidationMethod.DNS
        )
