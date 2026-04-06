from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class CKV2TfCustom0102(BaseResourceCheck):
    def __init__(self):
        name = "Ensure local_file resources use restrictive file permissions (0600 or stricter)"
        id = "CKV2_TF_CUSTOM_0102"
        supported_resources = ["local_file"]
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources,
        )

    def scan_resource_conf(self, conf):
        permission = conf.get("file_permission", [None])
        if isinstance(permission, list):
            permission = permission[0] if permission else None

        if permission is None:
            return CheckResult.FAILED

        try:
            perm_int = int(str(permission), 8)
            # Group and other bits must be zero (mask 0o077)
            return CheckResult.PASSED if perm_int & 0o077 == 0 else CheckResult.FAILED
        except (ValueError, TypeError):
            return CheckResult.FAILED


check = CKV2TfCustom0102()
