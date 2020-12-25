#! python3
# -*- coding: utf-8 -*-

# rename.py - 名前変更

import glob, os

files = glob.glob("*.png")
for file in files:
    os.rename(file, "tottori-"+file.split("-")[1])