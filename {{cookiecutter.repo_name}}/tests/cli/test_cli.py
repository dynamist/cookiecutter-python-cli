# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from subprocess import check_output


def _run_cmd(cmd):
    """Run a shell command `cmd` and return its output."""
    return check_output(cmd, shell=True).decode("utf-8")

def test_cli():
    """Test base cli"""
    result = _run_cmd("helloworld test")
    assert result == " INFO - Running test function\n"
