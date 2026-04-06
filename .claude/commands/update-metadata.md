Run the post-change metadata update sequence for this repository.

This must be run after any policy file is added, modified, or removed.

Execute in order:

1. Regenerate all per-service `policy-index.json` and `policy-index.csv` files:
   ```
   python scripts/generate-policy-index.py
   ```

2. Roll up all policy-index files into the root catalog and update `metadata/versions/latest/`:
   ```
   python scripts/sync-check-catalog.py
   ```

3. Validate the updated metadata against the JSON Schema:
   ```
   ./scripts/validate-metadata.sh
   ```

4. Report what changed: which policy-index files were updated, how many total policies are now in the catalog, and whether validation passed.

Note: if the scripts do not exist yet, report which scripts are missing and what they need to do based on the CLAUDE.md spec, so they can be created.
