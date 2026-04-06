from pathlib import Path

from checkov.runner_filter import RunnerFilter
from checkov.terraform.runner import Runner

FIXTURES_DIR = Path(__file__).parent
POLICY_DIR = Path(__file__).parents[5] / "terraform" / "gcp" / "gcs" / "yaml"
CHECK_ID = "CKV2_GCP_CUSTOM_0004"


def test_pass():
    result = Runner().run(
        root_folder=str(FIXTURES_DIR / "pass"),
        runner_filter=RunnerFilter(checks=[CHECK_ID]),
        external_checks_dir=[str(POLICY_DIR)],
    )
    assert len(result.passed_checks) >= 1
    assert len(result.failed_checks) == 0


def test_fail():
    result = Runner().run(
        root_folder=str(FIXTURES_DIR / "fail"),
        runner_filter=RunnerFilter(checks=[CHECK_ID]),
        external_checks_dir=[str(POLICY_DIR)],
    )
    assert len(result.failed_checks) >= 1
    assert len(result.passed_checks) == 0
