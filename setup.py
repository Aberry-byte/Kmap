#!/usr/bin/env python3
"""
Author: Alex Huft
Description: Cython functions for kmap
"""
from setuptools import setup
from Cython.Build import cythonize

setup(
    name="tools",
    ext_modules=cythonize("tools.pyx"),
    zip_safe=False
)
