"""
Checkov custom policy: CKV2_TF_CUSTOM_0101
Ensures null_resource and terraform_data resources do not use local-exec provisioners.
"""

from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class CKV2TfCustom0101(BaseResourceCheck):
    def __init__(self):
        name = "Ensure null_resource and terraform_data resources do not use local-exec provisioners"
        id = "CKV2_TF_CUSTOM_0101"
        supported_resources = ["null_resource", "terraform_data"]
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources,
        )

    def scan_resource_conf(self, conf):
        provisioner = conf.get("provisioner", [])
        if isinstance(provisioner, list):
            for p in provisioner:
                if isinstance(p, dict) and "local-exec" in p:
                    return CheckResult.FAILED
        elif isinstance(provisioner, dict):
            if "local-exec" in provisioner:
                return CheckResult.FAILED
        return CheckResult.PASSED


check = CKV2TfCustom0101()
