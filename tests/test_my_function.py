
# tests/test_my_function.py

import pytest
from my_function import add


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
