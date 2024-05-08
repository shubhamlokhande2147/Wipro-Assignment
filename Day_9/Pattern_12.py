import re

count = 0
pattern = re.compile("python")
print(pattern)
sent = "python is a prog and python is High level"
matcher = pattern.finditer(sent)

for match in matcher:
    print(match.start(), "...", match.end(), "...", match.group())
