import subprocess
import sys


def test_relaytown_can_start():
    result = subprocess.run(
        [sys.executable, "-m", "relaytown"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "RelayTown 正在启动" in result.stdout
