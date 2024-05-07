class NegativeAgeException(Exception):
    pass
 
def isValidAge(age):
    if age<0:
        raise NegativeAgeException()
    else:
        print(age)
 
 
 
age=int(input('enter age'))
try:
    isValidAge(age)
except NegativeAgeException as e:
    print('Plz provide age as positive')
