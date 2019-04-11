#!/bin/sh
cd "`dirname "$0"`"

python RPGGen.py
osascript -e 'tell application "Terminal" to quit'