from pathlib import Path

import pytest

from src.decorators import log


@log()
def my_function_console(x: int, y: int) -> int:
    return x + y


@log()
def my_function_error(x: str, y: int) -> int:
    if x == "undefined_var":
        raise ValueError("Invalid value for x")
    return x + y


def test_my_function_file(tmp_path: str | Path) -> None:
    log_file = tmp_path / "testlog.txt"

    @log(filename=log_file)
    def test_function(x: int, y: int) -> int:
        return x * y

    result = test_function(2, 3)
    assert result == 6

    with open(log_file, "r") as f:
        log_content = f.read()

    assert "Started execution of test_function" in log_content
    assert "Finished execution of test_function with result: 6" in log_content


def test_my_function_console(capsys: pytest.CaptureFixture) -> None:
    result = my_function_console(3, 2)
    captured = capsys.readouterr()

    assert result == 5
    assert "Started execution of my_function_console" in captured.out
    assert "Finished execution of my_function_console with result: 5" in captured.out


def test_my_function_error_handling(capsys: pytest.CaptureFixture) -> None:
    with pytest.raises(ValueError, match="Invalid value for x"):
        my_function_error("undefined_var", 2)
    captured = capsys.readouterr()
    assert "Started execution of my_function_error" in captured.out
    assert "Error in my_function_error; Type: ValueError" in captured.out
