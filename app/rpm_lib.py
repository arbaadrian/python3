"""
rpm module
"""

import rpm


def check_rpm(package_name, package_version=None):
    rpm_ts = rpm.TransactionSet()
    rpm_query = rpm_ts.dbMatch("name", package_name)
    for package in rpm_query:
        if package_version:
            if package_version == package["version"].decode():
                print("{} - {}, release: {} found!".format(
                    package["name"].decode(),
                    package["version"].decode(),
                    package["release"].decode())
                )
                return True
            continue
        print("{} - {}, release: {} found!".format(
            package["name"].decode(),
            package["version"].decode(),
            package["release"].decode())
        )
        return True

    print("Not found")
    return False
