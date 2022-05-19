#!/usr/bin/env python3

import re
log = "July 31 07:51:48 my_computer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result)
print(result[1])
