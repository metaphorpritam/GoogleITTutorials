#!/usr/bin/env python3

import subprocess
subprocess.run(["date"]) # Runs shell command date
subprocess.run(["sleep", "2"]) # Runs shell command 'sleep 2'
# The above parent process will create a child process that will block
# the command line interpreter 
print("Sleep End")
result = subprocess.run(["ls", "this_file_does_not_exist"])
print(result.returncode)
result = subprocess.run(["host", "8.8.8.8"], capture_output = True)
print(result.returncode)
print(result.stdout.decode())
# Removing a file name that doesn't exist
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
if result.returncode != 0:
    print(result.returncode)
    print(result.stdout.decode())
    print(result.stderr.decode())