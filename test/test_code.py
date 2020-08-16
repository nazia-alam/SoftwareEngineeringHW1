import sys
sys.path.insert(0,"../code")

from __init__ import add_numbers

def test_add_numbers():
    assert add_numbers(1,2)==3, "add_numbers function not working properly"
