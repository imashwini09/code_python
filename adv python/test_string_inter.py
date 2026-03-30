import pytest
import sys

def create_string(s):
    return sys.intern(s)  # Explicitly intern a string

def test_string_interning():
    str1 = "test_string"
    str2 = "test_string"
    assert str1 is str2, "Literal strings should be interned"

def test_dynamic_string_not_interned():
    str1 = "test_" + "string"
    str2 = "test_" + "string"
    assert str1 == str2, "Strings should be equal"
    assert str1 is not str2, "Dynamic strings should not be interned"

def test_explicit_interning():
    str1 = "test_" + "string"
    str2 = "test_" + "string"
    interned1 = create_string(str1)
    interned2 = create_string(str2)
    assert interned1 is interned2, "Explicitly interned strings should share memory"