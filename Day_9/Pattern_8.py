import re

pattern = '[aA]{1}'
# Returns a Match object if there is a match anywhere in the string
match = re.search(pattern, 'Ajaay')
print(match)

if match:
    print('Pattern matching')
else:
    print('Not matching')
