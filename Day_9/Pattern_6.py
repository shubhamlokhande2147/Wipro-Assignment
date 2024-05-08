import re
txt="The rain in Spain"
#checks for a match anywhere in the string
x=re.search('ai',txt)
print(x.group())
