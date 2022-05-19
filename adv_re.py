#!/usr/bin/env python3
import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
print("{} {}".format(result[2], result[1]))

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    else: return "{} {}".format(result[2], result[1])

print(rearrange_name("Lovelace, Ada"))

# Repetition Qualifiers
print(re.search(r"[a-zA-Z]{5}", "a ghost")) # '[a-zA-Z] repeated 5 times'
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")) # Indicate whole words using '\b'
print(re.findall(r"\w{5, 10}", "I really like strawberries")) # Range between 5 to 10
print(re.search(r"s\w{,20}", "I really like strawberries")) # Upto 20 alphanumeric characters

# Extracting a PID using regexes in Python
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(type(result.groups()))
print(result[1])
result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])
# Using a function
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    else: return result[1]

print(extract_pid(log))
print(extract_pid("99 elephants in a cage"))

# Splitting and Replacing
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))
# Using 're.sub(regex, sub_str, input_str)' for substitution
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Recieved an email for pritam.sarkar@aarti-industries.com"))
# Using an regex for substitution in re.sub
print(re.sub(r"^([\w.-]*), ([\w.-]*)$", r"\2 \1", "Lovelace, Ada"))
