#!/usr/bin/env python3
import os
import sys



def main():
    if reboot_all():
        print("Pending reboot")
        sys.exit(1)
    else:
        print("Not needed reboot")
        sys.exit(0)


main()
