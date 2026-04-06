from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class CKV2TfCustom0100(BaseResourceCheck):
    def __init__(self):
        name = "Ensure random_password resources enforce a minimum length of 16 characters"
        id = "CKV2_TF_CUSTOM_0100"
        supported_resources = ["random_password"]
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources,
        )

    def scan_resource_conf(self, conf):
        length = conf.get("length", [0])
        if isinstance(length, list):
            length = length[0] if length else 0
        return CheckResult.PASSED if isinstance(length, int) and length >= 16 else CheckResult.FAILED


check = CKV2TfCustom0100()
