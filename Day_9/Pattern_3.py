import re

s1 = 'bob has a birthday on Feb 25th'
s2 = 'sara has a birthday on March 3rd'
s3 = '12eup 586iu'
s4 = '0turt'

pattern1 = re.compile('\w+ \d+\w+')

pattern2 = re.compile('\w+ \w+')
x = pattern1.search(s1)
print(x.group())

x = pattern2.search(s2)
print(x.group())

pattern3 = re.compile('\d+\w+ \d+')
x = pattern3.search(s3)
print(x.group())
