Scaffold a new Checkov custom policy for this repository end-to-end.

Arguments: $ARGUMENTS
Expected format: `<cloud> <service> <id> <type> <short description>`
- cloud: common | gcp | aws | azure
- service: e.g. gcs, cloudsql, s3, storage, common
- id: full check ID, e.g. CKV2_GCP_CUSTOM_0005
- type: yaml | python
- short description: what the check enforces

Steps to follow:

1. Read `terraform/<cloud>/<service>/metadata/policy-index.json` to confirm the ID is not already taken.

2. Create the policy file:
   - If type=yaml: `terraform/<cloud>/<service>/yaml/<id>.yaml` — follow the YAML DSL format from CLAUDE.md
   - If type=python: `terraform/<cloud>/<service>/python/<id>.py` — follow the Python BaseResourceCheck pattern from CLAUDE.md, with a module-level `check = <ClassName>()` singleton

3. Create the test directory `tests/terraform/<cloud>/<service>/<id>/` with:
   - `test_<id>.py` — using the test template from CLAUDE.md
   - `pass/main.tf` — minimal fixture that satisfies the check
   - `fail/main.tf` — minimal fixture that violates the check

4. Update `terraform/<cloud>/<service>/metadata/policy-index.json` to append the new entry.
   Update `terraform/<cloud>/<service>/metadata/policy-index.csv` to append the new row.

5. For Python checks: confirm `terraform/<cloud>/<service>/python/__init__.py` exists; create it (empty) if not.

6. Print a summary of every file created or modified.

Use the naming conventions, ID ranges, and file layout documented in CLAUDE.md exactly.
