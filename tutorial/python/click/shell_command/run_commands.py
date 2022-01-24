#!/usr/bin/env python
import subprocess

date = subprocess.run('date',shell=True,capture_output=True)
print(date.stdout.decode())

task_info = subprocess.run('task',shell=True,capture_output=True)
print(task_info.stdout.decode())
