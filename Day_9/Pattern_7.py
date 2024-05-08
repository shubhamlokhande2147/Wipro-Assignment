import re
txt="The rain in Spain"
#findall() function returns a list containing all matcher
#The list contains the matches in the orderthey are found
#If nomatches are found, an emplty list is returned
x=re.findall('ai',txt)
print(x)
