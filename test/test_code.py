#!/usr/bin/env python
import sys
sys.path.insert(0, "../")
from code.main import add_numbers  


def test_add_numbers():
    assert add_numbers(1, 2) == 3, "add_numbers function not working properly"
