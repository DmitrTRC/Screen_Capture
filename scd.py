#!/usr/bin/env python

import datetime as dt
import os
import sys

import pyautogui
import yaml

try:
    config = yaml.safe_load(open("config.yaml", 'r'))
    base_path = config.get('path', None)
    base_name = config.get('name', None) + '_'

except yaml.YAMLError as exc:
    print("Error in configuration file 'config.yaml':", exc)
else:
    if (not base_name) or (not base_path):
        print('config.yaml not has damaged . Default configuration loaded')
        base_path = 'Desktop'
        base_name = 'Screen_'

suffix_data = dt.datetime.now().strftime("%c") + '.png'

if len(sys.argv) > 1 and sys.argv[1]:
    result_path = os.path.join(os.environ.get('HOME'), sys.argv[1])
else:
    result_path = os.path.join(os.environ.get('HOME'), base_path, base_name + suffix_data)
print(result_path)
screen = pyautogui.screenshot()
# screen.save(result_path)
