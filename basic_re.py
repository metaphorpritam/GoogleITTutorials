#!/usr/bin/env python3

import re
result = re.search(r"aza", "plaza")
print(result)
result = re.search(r"aza", "bazaar")
print(result)
result = re.search(r"aza", "maze")
print(result)
print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE)) # Ignore Case Sensitivity
print(re.search(r"[Pp]ython", "Python"))
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go!"))
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces.")) # Will not match any spaces
print(re.findall(r"cat|dog", "I like both cats and dogs!"))
# Repetition Qualifiers
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming")) # Only Character class
# '+' and '?'
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))
print(re.search(r"p?each", "I Love peaches"))
# Escaping Characters
print(re.search(r"\.com", "welcome")) # With Escape character '\'
print(re.search(r".com", "welcome")) # Without the escape character '\'
# Using '\w'
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "This_is_an_example"))
# Regular Expression in Action
# See Lecture
var_patt = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(var_patt, "_this_is_a_valid_variable_name_"))
""""this isn't a valid variable"""
print(re.search(var_patt, "this isn't a valid variable"))
print(re.search(var_patt, "my_var1"))
print(re.search(var_patt, "1my_var"))

