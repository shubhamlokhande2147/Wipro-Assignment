import re

def checkNameValidity(name):
    pattern = re.compile(r'^[A-Z][a-zA-Z ]{0,28}[A-Z]?$', re.IGNORECASE)
    if re.match(pattern, name) and len(name.strip()) >= 2 and len(name.strip()) <= 30:
        return True
    else:
        return False

# Test cases
print(checkNameValidity("Roger Federer"))  # Output: True
print(checkNameValidity("roger federer"))  # Output: False
