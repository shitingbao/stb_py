#!/usr/bin/env python3
import os


def getFileInfo(file_path):
    with open(file_path) as f:
        print(f.name)
        tx = f.read()
        print(tx)
        f.seek(0)
        tx = f.readline()
        print(tx)
        f.close()
