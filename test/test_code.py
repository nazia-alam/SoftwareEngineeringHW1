#!/usr/bin/env python
sys.path.insert(0, "../")
from code.main import add_numbers
import sys  


def test_add_numbers():
    assert add_numbers(1, 2) == 3, "add_numbers function not working properly"
