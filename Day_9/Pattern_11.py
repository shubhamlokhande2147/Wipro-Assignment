import re

# RegEx pattern
pattern = '[abc]'
matcher = re.finditer(pattern, 'abcdef')

for match in matcher:
    print(match.start(), "...", match.end(), "...", match.group())
