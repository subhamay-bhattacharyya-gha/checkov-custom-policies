# CLAUDE.md — checkov-custom-policies

This file provides context and guidance for Claude Code when working in this repository.

---

## Repository Purpose

`checkov-custom-policies` is a centralized library of reusable custom Checkov policies, YAML rules, Python checks, and framework-specific compliance validations. It also provides a **metadata-driven dispatch layer** (`services-checkov-map.json`) that allows consuming pipelines to dynamically select which policy directories to pass to Checkov based on detected Terraform modules and cloud services.

Supported frameworks and clouds:

- **Terraform** — GCP (primary), AWS, Azure
- **CloudFormation**
- **Kubernetes**
- **GitHub Actions**
- **Dockerfile**

---

## Repository Structure

```text
checkov-custom-policies/
├── README.md
├── LICENSE
├── .gitignore
│
├── docs/                                        # Human-facing documentation
│   ├── overview.md
│   ├── repository-structure.md
│   ├── custom-policy-development.md
│   ├── policy-naming-standards.md
│   ├── severity-guidelines.md
│   ├── metadata-schema.md
│   ├── onboarding.md
│   └── examples.md
│
├── metadata/                                    # Repo-level metadata and catalog files
│   ├── services-checkov-map.json                # Service → policy-directory mapping (canonical)
│   ├── services-checkov-map.schema.json         # JSON Schema enforced against the map file
│   ├── checkov-check-catalog.json               # Aggregated catalog of all policies in the repo
│   ├── service-aliases.json                     # Normalizes service name variants before map lookup
│   └── versions/
│       ├── v1.0.0/
│       │   ├── services-checkov-map.json
│       │   └── checkov-check-catalog.json
│       └── latest/
│           ├── services-checkov-map.json
│           └── checkov-check-catalog.json
│
├── scripts/                                     # Developer and CI utility scripts
│   ├── validate-policies.sh                     # Validates YAML/Python policy syntax
│   ├── validate-metadata.sh                     # Validates metadata files against JSON Schema
│   ├── run-local-checkov.sh                     # Runs Checkov locally against examples/
│   ├── run-tests.sh                             # Runs the full pytest suite with coverage
│   ├── generate-policy-index.py                 # Regenerates per-service policy-index files
│   ├── generate-metadata-report.py              # Generates a human-readable metadata report
│   └── sync-check-catalog.py                    # Rolls up policy-index files into the root catalog
│
├── tests/
│   ├── metadata/                                # Schema validation fixtures
│   │   ├── valid/
│   │   │   └── services-checkov-map.valid.json
│   │   └── invalid/
│   │       └── services-checkov-map.invalid.json
│   ├── terraform/                               # Mirrors terraform/ policy tree exactly
│   │   ├── common/
│   │   │   ├── pass/
│   │   │   └── fail/
│   │   ├── gcp/
│   │   │   ├── common/
│   │   │   │   ├── pass/
│   │   │   │   └── fail/
│   │   │   ├── gcs/
│   │   │   ├── cloudsql/
│   │   │   ├── pubsub/
│   │   │   ├── bigquery/
│   │   │   ├── bigtable/
│   │   │   ├── spanner/
│   │   │   ├── compute/
│   │   │   ├── kms/
│   │   │   ├── vpc/
│   │   │   ├── datastore/
│   │   │   ├── firestore/
│   │   │   ├── dataflow/
│   │   │   ├── dataproc/
│   │   │   └── alloydb/
│   │   ├── aws/
│   │   │   ├── common/
│   │   │   └── s3/
│   │   └── azure/
│   │       ├── common/
│   │       └── storage/
│   └── fixtures/                                # Reusable shared Terraform fixture modules
│       ├── module-based/
│       ├── resource-based/
│       └── mixed/
│
├── terraform/                                   # Terraform policies (cloud → service hierarchy)
│   ├── common/                                  # Cloud-agnostic checks (apply to all providers)
│   │   ├── yaml/
│   │   │   ├── CKV2_TF_CUSTOM_0001.yaml
│   │   │   └── CKV2_TF_CUSTOM_0002.yaml
│   │   ├── python/
│   │   │   └── CKV2_TF_CUSTOM_0100.py
│   │   └── metadata/
│   │       ├── policy-index.json
│   │       └── policy-index.csv
│   ├── gcp/
│   │   ├── common/                              # GCP-wide checks (labels, modules, project IDs)
│   │   │   ├── yaml/
│   │   │   │   ├── CKV2_GCP_CUSTOM_0001.yaml
│   │   │   │   ├── enforce-module-usage.yaml
│   │   │   │   ├── require-standard-labels.yaml
│   │   │   │   └── restrict-hardcoded-project-id.yaml
│   │   │   ├── python/
│   │   │   │   └── CKV2_GCP_CUSTOM_0100.py
│   │   │   └── metadata/
│   │   │       ├── policy-index.json
│   │   │       └── policy-index.csv
│   │   ├── gcs/
│   │   │   ├── yaml/
│   │   │   ├── python/
│   │   │   └── metadata/
│   │   ├── cloudsql/
│   │   ├── pubsub/
│   │   ├── bigquery/
│   │   ├── bigtable/
│   │   ├── spanner/
│   │   ├── compute/
│   │   ├── kms/
│   │   ├── vpc/
│   │   ├── datastore/
│   │   ├── firestore/
│   │   ├── dataflow/
│   │   ├── dataproc/
│   │   └── alloydb/
│   ├── aws/
│   │   ├── common/
│   │   └── s3/
│   └── azure/
│       ├── common/
│       └── storage/
│
├── examples/                                    # Runnable reference configs (not scanned by pytest)
│   ├── github-actions/
│   │   ├── checkov-local-policies.yml
│   │   ├── checkov-central-policies.yml
│   │   ├── metadata-driven-checkov.yml
│   │   └── reusable-workflow-example.yml
│   ├── metadata/
│   │   ├── services-checkov-map.sample.json
│   │   └── detection-output.sample.json
│   └── terraform/
│       ├── gcp/
│       │   ├── module-based/
│       │   ├── resource-based/
│       │   └── mixed/
│       └── aws/
│
├── releases/
│   ├── CHANGELOG.md
│   └── manifests/
│       ├── policy-bundle-v1.0.0.json
│       └── latest.json
│
└── .github/
    ├── actions/
    │   └── detect-terraform-modules/            # Composite action: detects modules, emits policy dirs
    │       ├── action.yml
    │       ├── detect_modules.py
    │       ├── README.md
    │       └── metadata/
    │           └── services-checkov-map.json    # Pinned copy — synced by release.yml, not by hand
    ├── workflows/
    │   ├── validate-custom-policies.yml
    │   ├── validate-metadata.yml
    │   ├── test-custom-policies.yml
    │   ├── generate-documentation.yml
    │   └── release.yml
    ├── ISSUE_TEMPLATE/
    │   ├── new-policy.md
    │   ├── new-service-mapping.md
    │   ├── bug-report.md
    │   └── enhancement.md
    └── pull_request_template.md
```

---

## The Metadata Layer

This repository ships a **metadata-driven dispatch system** alongside its policy library. Consuming pipelines use it to run only the policies relevant to a given Terraform workspace.

### Key Files

| File | Purpose |
| --- | --- |
| `metadata/services-checkov-map.json` | Maps service names to the `--external-checks-dir` paths that Checkov should receive |
| `metadata/services-checkov-map.schema.json` | JSON Schema validated in CI against the map file |
| `metadata/checkov-check-catalog.json` | Flat catalog of every policy: ID, name, severity, category, cloud, service, file path |
| `metadata/service-aliases.json` | Normalizes service name variants (e.g. `gcs` → `google_cloud_storage`) before map lookup |
| `metadata/versions/` | Immutable snapshots of the map and catalog, pinned per release tag |

### `services-checkov-map.json` Shape

```json
{
  "version": "1.0.0",
  "mappings": {
    "gcs": {
      "description": "Google Cloud Storage",
      "policy_dirs": [
        "terraform/gcp/common",
        "terraform/gcp/gcs"
      ]
    },
    "cloudsql": {
      "description": "Cloud SQL",
      "policy_dirs": [
        "terraform/gcp/common",
        "terraform/gcp/cloudsql"
      ]
    }
  }
}
```

Every `policy_dirs` entry is a path relative to the repository root. Always include `terraform/gcp/common` (or the equivalent cloud-level `common` directory) alongside any service-specific path.

### `detect-terraform-modules` Composite Action

The `.github/actions/detect-terraform-modules/` composite action:

1. Scans a Terraform workspace for `module` blocks and `resource` type prefixes
2. Resolves each detected service through `service-aliases.json`, then looks it up in `services-checkov-map.json`
3. Emits the resolved `--external-checks-dir` path list as an action output for downstream Checkov steps

The action carries its **own pinned copy** of `services-checkov-map.json` at `.github/actions/detect-terraform-modules/metadata/services-checkov-map.json`. This copy is synced automatically by `release.yml` on every tag push. **Do not update this file by hand.**

---

## Policy Directory Layout

Every service directory under `terraform/<cloud>/<service>/` follows the same internal layout:

```text
<service>/
├── yaml/       # YAML-DSL rules (attribute matching, simple logic)
├── python/     # Python BaseResourceCheck / BaseGraphCheck subclasses
└── metadata/
    ├── policy-index.json   # Generated — do not edit
    └── policy-index.csv    # Generated — do not edit
```

---

## Naming Conventions

### Check IDs

| Prefix | Scope | YAML range | Python range |
| --- | --- | --- | --- |
| `CKV2_TF_CUSTOM_` | Cloud-agnostic Terraform | `0001`–`0099` | `0100`–`0499` |
| `CKV2_GCP_CUSTOM_` | GCP Terraform | `0001`–`0099` | `0100`–`0499` |
| `CKV2_AWS_CUSTOM_` | AWS Terraform | `0001`–`0099` | `0100`–`0499` |
| `CKV2_AZR_CUSTOM_` | Azure Terraform | `0001`–`0099` | `0100`–`0499` |

IDs are zero-padded to four digits (`0001`, not `1`). Check the relevant `metadata/policy-index.json` before assigning a new ID. IDs are never reused or reassigned.

### File Names

| Artifact | Pattern | Example |
| --- | --- | --- |
| Numbered YAML rule | `<ID>.yaml` | `CKV2_GCP_CUSTOM_0001.yaml` |
| Named convention YAML (`gcp/common/` only) | `<verb>-<noun>.yaml` | `require-standard-labels.yaml` |
| Python check file | `<ID>.py` | `CKV2_GCP_CUSTOM_0100.py` |
| Python check class | PascalCase ID, no underscores | `CKV2GcpCustom0100` |

Named convention files still carry a `CKV2_*_CUSTOM_` ID inside the file's `metadata.id` field.

---

## Writing YAML Rules

Use YAML rules for attribute presence, equality, or pattern checks that need no iteration or cross-resource logic.

```yaml
# terraform/gcp/gcs/yaml/CKV2_GCP_CUSTOM_0001.yaml
metadata:
  name: "Ensure GCS buckets have uniform bucket-level access enabled"
  id: "CKV2_GCP_CUSTOM_0001"
  category: "GENERAL_SECURITY"
  severity: "MEDIUM"

scope:
  provider: terraform

definition:
  and:
    - cond_type: attribute
      resource_types:
        - google_storage_bucket
      attribute: uniform_bucket_level_access
      operator: equals
      value: "true"
```

Prefer Python checks when the logic requires iteration, conditionals, or cross-resource graph traversal.

---

## Writing Python Checks

### Minimal Example

```python
# terraform/gcp/cloudsql/python/CKV2_GCP_CUSTOM_0100.py
from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class CKV2GcpCustom0100(BaseResourceCheck):
    def __init__(self):
        name = "Ensure Cloud SQL instances require SSL connections"
        id = "CKV2_GCP_CUSTOM_0100"
        supported_resources = ["google_sql_database_instance"]
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources,
        )

    def scan_resource_conf(self, conf):
        # HCL values are often list-wrapped — always unwrap defensively
        settings = conf.get("settings", [{}])
        if isinstance(settings, list):
            settings = settings[0] if settings else {}

        ip_config = settings.get("ip_configuration", [{}])
        if isinstance(ip_config, list):
            ip_config = ip_config[0] if ip_config else {}

        require_ssl = ip_config.get("require_ssl", [False])
        if isinstance(require_ssl, list):
            require_ssl = require_ssl[0]

        return CheckResult.PASSED if require_ssl is True else CheckResult.FAILED


check = CKV2GcpCustom0100()
```

### Rules

- Every check **must** be instantiated as a module-level singleton (`check = CKV2GcpCustom0100()`). Checkov auto-registers it on import.
- HCL values in `scan_resource_conf` are frequently list-wrapped — always unwrap defensively.
- Use `CheckResult.PASSED` and `CheckResult.FAILED` (never raw strings or booleans).
- Avoid side effects, network calls, or file I/O inside checks.

---

## Testing

### Running Tests

```bash
# Full suite via the wrapper script
./scripts/run-tests.sh

# Directly with pytest
pytest tests/ -v

# Single cloud/service subtree
pytest tests/terraform/gcp/cloudsql/ -v

# With coverage
pytest tests/ --cov=terraform --cov-report=term-missing
```

### Test Directory Mirror

The `tests/terraform/` tree mirrors `terraform/` exactly. A check at `terraform/gcp/cloudsql/python/CKV2_GCP_CUSTOM_0100.py` has its test at:

```text
tests/terraform/gcp/cloudsql/
├── test_CKV2_GCP_CUSTOM_0100.py
├── pass/
│   └── CKV2_GCP_CUSTOM_0100_pass.tf
└── fail/
    └── CKV2_GCP_CUSTOM_0100_fail.tf
```

### Test File Template

```python
# tests/terraform/gcp/cloudsql/test_CKV2_GCP_CUSTOM_0100.py
from pathlib import Path
from checkov.runner_filter import RunnerFilter
from checkov.terraform.runner import Runner
from terraform.gcp.cloudsql.python.CKV2_GCP_CUSTOM_0100 import check

FIXTURES_DIR = Path(__file__).parent


def test_pass():
    result = Runner().run(
        root_folder=str(FIXTURES_DIR / "pass"),
        runner_filter=RunnerFilter(checks=[check.id]),
    )
    assert len(result.passed_checks) >= 1
    assert len(result.failed_checks) == 0


def test_fail():
    result = Runner().run(
        root_folder=str(FIXTURES_DIR / "fail"),
        runner_filter=RunnerFilter(checks=[check.id]),
    )
    assert len(result.failed_checks) >= 1
    assert len(result.passed_checks) == 0
```

### Fixture File Rules

- Fixtures must be **minimal** — include only resources relevant to the check under test.
- Use realistic resource names; avoid placeholder values that break Terraform parsing.
- One fixture file per check per direction is sufficient unless multiple resource combinations need explicit coverage.

### Metadata Tests

`tests/metadata/valid/` and `tests/metadata/invalid/` contain fixture JSON files used to assert that `validate-metadata.sh` correctly accepts and rejects `services-checkov-map.json` documents. When modifying `metadata/services-checkov-map.schema.json`, update both fixture sets.

### `tests/fixtures/`

Shared reusable Terraform fixture modules in `tests/fixtures/` (split into `module-based/`, `resource-based/`, and `mixed/`) can be referenced from individual test fixture files via `module` blocks. Use these to avoid duplicating large boilerplate configurations.

---

## Scripts

| Script | Purpose |
| --- | --- |
| `scripts/validate-policies.sh` | Validates YAML rule syntax and Python check imports |
| `scripts/validate-metadata.sh` | Validates `metadata/services-checkov-map.json` against its JSON Schema |
| `scripts/run-local-checkov.sh` | Runs Checkov against `examples/terraform/` using all policies in the repo |
| `scripts/run-tests.sh` | Wrapper around `pytest tests/ -v` with coverage flags pre-configured |
| `scripts/generate-policy-index.py` | Scans all `yaml/` and `python/` directories; regenerates every `metadata/policy-index.*` |
| `scripts/generate-metadata-report.py` | Produces a human-readable summary of all policies, grouped by cloud and service |
| `scripts/sync-check-catalog.py` | Rolls up all `metadata/policy-index.json` files into `metadata/checkov-check-catalog.json` and updates `metadata/versions/latest/` |

**Required order of operations after any policy change:**

```bash
python scripts/generate-policy-index.py
python scripts/sync-check-catalog.py
./scripts/validate-metadata.sh
./scripts/run-tests.sh
```

---

## Metadata Index Format

Each service directory's `metadata/policy-index.json` is generated and follows this shape:

```json
[
  {
    "id": "CKV2_GCP_CUSTOM_0100",
    "name": "Ensure Cloud SQL instances require SSL connections",
    "type": "python",
    "cloud": "gcp",
    "service": "cloudsql",
    "severity": "HIGH",
    "category": "ENCRYPTION",
    "file": "terraform/gcp/cloudsql/python/CKV2_GCP_CUSTOM_0100.py"
  }
]
```

`metadata/checkov-check-catalog.json` uses the same shape but aggregates entries from all services into a single flat array.

---

## CI Workflows

| Workflow | Trigger | What it does |
| --- | --- | --- |
| `validate-custom-policies.yml` | Push, PR to `main` | Runs `validate-policies.sh`; checks YAML syntax and Python imports |
| `validate-metadata.yml` | Push, PR to `main` | Runs `validate-metadata.sh`; enforces JSON Schema on map file |
| `test-custom-policies.yml` | Push, PR to `main` | Runs `run-tests.sh`; enforces **80% line coverage** gate |
| `generate-documentation.yml` | Merge to `main` | Runs `generate-policy-index.py` + `sync-check-catalog.py`; commits updated metadata |
| `release.yml` | Tag push (`v*`) | Snapshots `metadata/` into `metadata/versions/<tag>/`; updates `latest/`; syncs the action's pinned map copy; publishes to `releases/manifests/` |

PRs cannot be merged unless `validate-custom-policies`, `validate-metadata`, and `test-custom-policies` all pass.

---

## Releases

`releases/manifests/latest.json` always points to the most recent stable release. `policy-bundle-v<tag>.json` is an immutable snapshot created by `release.yml`. `releases/CHANGELOG.md` follows [Keep a Changelog](https://keepachangelog.com) format — update it manually as part of the PR that bumps the version, not as part of a release tag.

---

## Adding a New Policy — End-to-End Checklist

- [ ] Identify the correct cloud, service, and ID prefix from the naming table above
- [ ] Assign the next available sequential ID (check `terraform/<cloud>/<service>/metadata/policy-index.json`)
- [ ] Create the YAML rule or Python check file in the appropriate `yaml/` or `python/` directory
- [ ] Mirror the path in `tests/terraform/<cloud>/<service>/` and create `pass/` and `fail/` fixture files
- [ ] Write a pytest test file at `tests/terraform/<cloud>/<service>/test_<ID>.py`
- [ ] Run `./scripts/run-tests.sh` — all tests must pass
- [ ] Run `./scripts/validate-policies.sh` — no syntax errors
- [ ] Run the post-change script sequence: `generate-policy-index.py` → `sync-check-catalog.py` → `validate-metadata.sh`
- [ ] Confirm `ruff check` and `mypy` pass for any Python files added or modified
- [ ] Open a PR using `.github/pull_request_template.md`

## Adding a New Service

When a new cloud service is introduced for the first time:

- [ ] Create `terraform/<cloud>/<service>/yaml/`, `python/`, and `metadata/` directories
- [ ] Mirror the path under `tests/terraform/<cloud>/<service>/`
- [ ] Add an entry to `metadata/services-checkov-map.json` following the documented shape (include the cloud-level `common` directory in `policy_dirs`)
- [ ] Add any known service name variants to `metadata/service-aliases.json`
- [ ] Run `./scripts/validate-metadata.sh` to confirm schema compliance
- [ ] Use the `new-service-mapping.md` issue template when filing the PR

---

## Key Checkov Concepts

| Concept | Notes |
| --- | --- |
| `BaseResourceCheck` | Use for single-resource attribute checks |
| `BaseGraphCheck` | Use for cross-resource relationship checks (e.g. a KMS key attached to a GCS bucket) |
| `CheckResult.PASSED / FAILED / UNKNOWN` | Always use the enum — never raw strings or booleans |
| `RunnerFilter(checks=[check.id])` | Pass via `runner_filter=` in tests to isolate the check under test |
| `conf` dict values | HCL values are often list-wrapped — always unwrap with `[0]` defensively |
| YAML rule DSL | Supports `and`, `or`, `not`, `attribute`, `connection` condition types |
| Module-level singleton | `check = CKV2GcpCustom0100()` at module level is required for Checkov auto-registration |

---

## Out of Scope

- Sentinel policies (use a dedicated Sentinel repository)
- OPA / Rego policies (use a dedicated OPA repository)
- Checkov configuration for specific consuming pipelines (those live in the pipeline repos)
- Auto-remediation scripts
- Infracost or cost-estimation policies
