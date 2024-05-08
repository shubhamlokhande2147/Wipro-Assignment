import re

# RegEx pattern
pattern = '[a-z]'
matcher = re.finditer(pattern, "abcdeyAB12")

for match in matcher:
    print(match.start(), "...", match.end(), "...", match.group())
