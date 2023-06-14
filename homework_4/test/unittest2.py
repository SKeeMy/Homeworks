
import pytest
from tasks.homework_4.code.task2 import count_dots_on_i


def test_count_dots_on_i():
    assert count_dots_on_i("https://www.google.com/") == 188
    assert count_dots_on_i("https://www.python.org/") == 115
    with pytest.raises(ValueError, match="Unreachable"):
        count_dots_on_i("nonexistent.website")
