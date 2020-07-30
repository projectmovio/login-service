# Deploy
* `pip install -U -r deploy/requirements.txt`

## Provision

* `cd deploy/provision`
* `cdk deploy '*'`

## Environment

* `export CERT_ARN=<PROVISION_CERT_ARN>`
* `cd deploy/env`
* `cdk deploy '*'`