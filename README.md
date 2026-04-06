# terraform-checkov-custom-policies

![CI](https://github.com/subhamay-bhattacharyya-gha/terraform-checkov-custom-policies/actions/workflows/ci.yaml/badge.svg)&nbsp;![Commit Activity](https://img.shields.io/github/commit-activity/t/subhamay-bhattacharyya-gha/terraform-checkov-custom-policies)&nbsp;![Last Commit](https://img.shields.io/github/last-commit/subhamay-bhattacharyya-gha/terraform-checkov-custom-policies)&nbsp;![Release Date](https://img.shields.io/github/release-date/subhamay-bhattacharyya-gha/terraform-checkov-custom-policies)&nbsp;![Repo Size](https://img.shields.io/github/repo-size/subhamay-bhattacharyya-gha/terraform-checkov-custom-policies)&nbsp;![Issues](https://img.shields.io/github/issues/subhamay-bhattacharyya-gha/terraform-checkov-custom-policies)&nbsp;![Top Language](https://img.shields.io/github/languages/top/subhamay-bhattacharyya-gha/terraform-checkov-custom-policies)

A centralized library of reusable custom [Checkov](https://www.checkov.io/) policies for Terraform infrastructure-as-code scanning. Supports a metadata-driven dispatch system so consuming CI pipelines can dynamically select only the policy directories relevant to their detected Terraform modules.

---

## Custom Checks

### Cloud-Agnostic — Terraform Common

| Check ID | Description | Type | Severity | Category |
|---|---|---|---|---|
| `CKV2_TF_CUSTOM_0100` | Ensure `random_password` resources enforce a minimum length of 16 characters | Python | MEDIUM | GENERAL_SECURITY |
| `CKV2_TF_CUSTOM_0101` | Ensure `null_resource` and `terraform_data` resources do not use `local-exec` provisioners | Python | MEDIUM | GENERAL_SECURITY |
| `CKV2_TF_CUSTOM_0102` | Ensure `local_file` resources use restrictive file permissions (`0600` or stricter) | Python | MEDIUM | GENERAL_SECURITY |

### GCP — Google Cloud Storage (GCS)

| Check ID | Description | Type | Severity | Category |
|---|---|---|---|---|
| `CKV2_GCP_CUSTOM_0001` | Ensure GCS buckets have uniform bucket-level access enabled | YAML | MEDIUM | GENERAL_SECURITY |
| `CKV2_GCP_CUSTOM_0002` | Ensure GCS buckets have versioning enabled | YAML | LOW | GENERAL_SECURITY |
| `CKV2_GCP_CUSTOM_0003` | Ensure GCS buckets enforce public access prevention | YAML | HIGH | GENERAL_SECURITY |
| `CKV2_GCP_CUSTOM_0004` | Ensure GCS buckets are encrypted with a customer-managed encryption key (CMEK) | YAML | HIGH | ENCRYPTION |

---

## Repository Structure

```
terraform/
├── common/python/        # Cloud-agnostic Python checks
└── gcp/
    ├── common/           # GCP-wide checks (labels, modules)
    └── gcs/yaml/         # GCS-specific YAML rules

tests/terraform/          # Mirrors terraform/ — pass/fail fixtures per check
metadata/                 # services-checkov-map.json, catalog, schema
```

---

## Running Tests

```bash
pip install checkov pytest pytest-cov
pytest tests/ -v --cov=terraform --cov-report=term-missing
```

---

## License

MIT
