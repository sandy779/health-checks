#!/usr/bin/env python3
import os
import sys

def reboot_all():
    return os.path.exist("/run/reboot required")

def main():
    if reboot_all():
        print("Pending reboot")
        sys.exit(1)
    else:
        print("Not needed reboot")
        sys.exit(0)


main()
