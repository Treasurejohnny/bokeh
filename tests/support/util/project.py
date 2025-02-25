#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2024, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------
''' Provide functions for inspecting project structure and files.

'''

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import annotations

import logging # isort:skip
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports
from pathlib import Path
from subprocess import run
from typing import Sequence

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

__all__ = (
    'TOP_PATH',
    'ls_files',
    'ls_modules',
    'verify_clean_imports',
)

TOP_PATH = Path(__file__).resolve().parent.parent.parent.parent

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

def ls_files(*patterns: str) -> list[str]:
    proc = run(["git", "ls-files", "--", *patterns], capture_output=True)
    return proc.stdout.decode("utf-8").split("\n")

def ls_modules(*, skip_prefixes: Sequence[str] = [], skip_main: bool = True) -> list[str]:
    modules: list[str] = []

    files = ls_files("src/bokeh/**.py")

    for file in files:
        if not file:
            continue

        if file.endswith("__main__.py") and skip_main:
            continue

        module = file.strip("src/").replace("/", ".").replace(".py", "").replace(".__init__", "")

        if any(module.startswith(prefix) for prefix in skip_prefixes):
            continue

        modules.append(module)

    return modules

def verify_clean_imports(target: str, modules: list[str]) -> str:
    return f"""
import sys
for module in {modules!r}:
    __import__(module)
    if any(key.startswith({target!r}) for key in sys.modules.keys()):
        print(module)
        sys.exit(1)
sys.exit(0)
"""

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
