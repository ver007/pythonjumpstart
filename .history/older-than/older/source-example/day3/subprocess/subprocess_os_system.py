#!/usr/bin/env python
"""Replacing os.system with subprocess.
"""
#end_pymotw_header

import subprocess

# Simple command
subprocess.call(['ls', 'peterpan'], stderr=open('/dev/null', 'w'))
#subprocess.call(raw_input('Enter the cmd :'), shell=True)
