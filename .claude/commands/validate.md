Run the full validation and test pipeline for this repository.

Execute the following steps in order. Stop and report the error if any step fails.

1. Run policy syntax validation:
   ```
   ./scripts/validate-policies.sh
   ```

2. Run metadata schema validation:
   ```
   ./scripts/validate-metadata.sh
   ```

3. Run the full test suite with coverage:
   ```
   ./scripts/run-tests.sh
   ```

4. If all three pass, report a green summary: which checks ran, coverage percentage, and any warnings.
   If any step fails, show the exact error output and stop.

Note: if the scripts do not exist yet, run the equivalent commands directly:
- Step 1 equivalent: check YAML files parse with `python -c "import yaml; yaml.safe_load(open('<file>'))"` and Python files import without error
- Step 2 equivalent: validate `metadata/services-checkov-map.json` against `metadata/services-checkov-map.schema.json`
- Step 3 equivalent: `pytest tests/ -v --cov=terraform --cov-report=term-missing`
