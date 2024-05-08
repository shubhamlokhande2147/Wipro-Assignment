import re
txt="ai The rain in Spain"
#checks for a match only at the beginining of the string
x=re.match('ai',txt)
print(x)
