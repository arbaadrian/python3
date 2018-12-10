#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pkg_resources import parse_version
import rpm

def check_rpm_version(name, version=None):
    """
        Checks the version of an installed Linux pakage and compares it to what is shipped
        by the Installer:
            - if the checked package is not installed, the module will pass
            - if the checked package is installed but the version is lower or the same version
              as the one shipped by the Installer, the module will pass
            - if the checked package is installed but the version is newer than the version
              shipped by the Installer, the module will fail

        Arguments:
            name: the name of the package to be checked
            version (none): the version of the package to be compared with the found version

        Returns:
            bool: True if the installed package version is the same or older than the one shipped
            with the Installer, False otherwise
    """
    
    rpm_ts = rpm.TransactionSet()
    rpm_query = rpm_ts.dbMatch("name", name)

    for package in rpm_query:
        if version:
            if parse_version(package["version"].decode()) <= parse_version(version):
                print(name + " - PASS: The installed version is valid.")
                return True
            else:
                print(name + " - FAIL: The installed version " + package["version"].decode() +
                      " is newer than the version shipped with the NCI installer. Exiting.")
                return False

    print(name + " - PASS: Tool not installed.")
    return True
