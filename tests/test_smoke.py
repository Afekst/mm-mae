# tests/test_smoke.py
from importlib import import_module

def test_import():
    assert import_module("mm_mae") is not None
