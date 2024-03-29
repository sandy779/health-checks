#!/usr/bin/env python3
import os
import sys
import shutil
import socket
import psutil

def reboot_all():
    return os.path.exists("/run/reboot required")

def check_disk_full(disk,min_gb,min_percent):
    du=shutil.disk_usage(disk)
    percent_free=100*du.free/du.total
    gigabytes_free=du.free/2**30
    if gigabytes_free<min_gb or percent_free<min_percent:
        return True
    return False
def check_cpu_usage():
    usage = psutil.disk_usage(1)
    return usage<75


def check_root_full():
    return check_disk_full(disk="/",min_gb=2,min_percent=10)

def check_no_network():
    """Returns false when it fails to resolve googles URL"""
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True

def main():
    checks=[
    (reboot_all,"Pending reboot"),
    (check_root_full,"Root partition full"),
    (check_no_network,"No network Found"),
    (check_cpu_usage,"There is enough unused space on cpu"),
    ]

    everything_ok=True

    for check,msg in checks:
        if check():
            print(msg)
            sys.exit(1)
            everything_ok=False
    if not everything_ok:
        sys.exit(1)

    print("Everything OK!")
    sys.exit(0)


main()
