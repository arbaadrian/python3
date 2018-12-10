#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch
from checker.rpm_package import check_rpm_version

"""
    Test module for checker.rpm_package module methods.
    Using @patch decorator to avoid nested mocking.

    In order to run just these tests:

    export PYTHONPATH=src
    python -m unittest tests/test_rpm_package.py
"""

__author__ = "Adrian Arba"
__copyright__ = "Adrian Arba"

name = "package"
version = "1.1.0"

class TestRpmPackageVersion(unittest.TestCase):

    def cleanup(self):
        pass

    def setUp(self):
        self.cleanup()

    def tearDown(self):
        self.cleanup()

    @patch('rpm.TransactionSet.dbMatch', return_value=([{"name": b"package", "version": b"1.0.0"}]))
    def test_rpm_package_version_installed_is_lower_pass(self, mock):
        assert check_rpm_version(name, version)

    @patch('rpm.TransactionSet.dbMatch', return_value=([{"name": b"package", "version": b"1.1.0"}]))
    def test_rpm_package_version_installed_is_the_same_pass(self, mock):
        assert check_rpm_version(name, version)

    @patch('rpm.TransactionSet.dbMatch', return_value=([{"name": b"package", "version": b"1.2.0"}]))
    def test_rpm_package_version_installed_is_newer_fail(self, mock):
        assert not check_rpm_version(name, version)

if __name__ == '__main__':
    unittest.main()
