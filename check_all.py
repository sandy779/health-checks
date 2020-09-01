#!/usr/bin/env python3
import os
import sys
import shutil

def reboot_all():
    return os.path.exists("/run/reboot required")

def check_disk_full(disk,min_gb,min_percent):
    du=shutil.disk_usage(disk)
    percent_free=100*du.free/du.total
    gigabytes_free=du.free/2**30
    if gigabytes_free<min_gb or percent_free<min_percent:
        return True
    return False


def check_root_full():
    return check_disk_full(disk="/",min_gb=2,min_percent=10)

def main():
    if reboot_all():
        print("Pending reboot")
        sys.exit(1)
    if check_root_full():
        print("Root Full!")
        sys.exit(1)
    print("Everything OK!")
    sys.exit(0)


main()
