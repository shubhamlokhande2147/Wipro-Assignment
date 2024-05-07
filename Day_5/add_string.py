def add_string(s):
    if len(s) < 3:
        return s
    elif s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'

# Test cases
print(add_string("sleep"))    # Output: "sleeping"
print(add_string("amazing"))  # Output: "amazingly"
print(add_string("is"))       # Output: "is"
