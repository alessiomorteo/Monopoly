"conftest.py is a pytest standard file for sharing fixtures across multiple files"
import pytest

@pytest.fixture()
def foo():
    return True
