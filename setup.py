#!/usr/bin/python

#######################################################
# Copyright (c) 2015, ArrayFire
# All rights reserved.
#
# This file is distributed under 3-clause BSD license.
# The complete license agreement can be obtained at:
# http://arrayfire.com/licenses/BSD-3-Clause
########################################################

from setuptools import setup, find_packages

## TODO:
## 1) Look for af libraries during setup
## 2) Include test suite

release_version = "3.4.0"

setup(
    author="Pavan Yalamanchili",
    author_email="pavan@arrayfire.com",
    name="arrayfire",
    version=release_version,
    description="Python bindings for ArrayFire",
    license="BSD",
    url="http://arrayfire.com",
    packages=['arrayfire'],
)
