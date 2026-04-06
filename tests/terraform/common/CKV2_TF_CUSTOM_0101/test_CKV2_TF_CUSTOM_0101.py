from pathlib import Path

from checkov.runner_filter import RunnerFilter
from checkov.terraform.runner import Runner

from terraform.common.python.CKV2_TF_CUSTOM_0101 import check

FIXTURES_DIR = Path(__file__).parent
CHECK_ID = check.id


def test_pass():
    result = Runner().run(
        root_folder=str(FIXTURES_DIR / "pass"),
        runner_filter=RunnerFilter(checks=[CHECK_ID]),
    )
    assert len(result.passed_checks) >= 1
    assert len(result.failed_checks) == 0


def test_fail():
    result = Runner().run(
        root_folder=str(FIXTURES_DIR / "fail"),
        runner_filter=RunnerFilter(checks=[CHECK_ID]),
    )
    assert len(result.failed_checks) >= 1
    assert len(result.passed_checks) == 0
