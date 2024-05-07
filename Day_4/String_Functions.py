def count_occurrences(string, target):
    return string.count(target)

def replace_chars(string, old_chars, new_chars):
    return string.replace(old_chars, new_chars)

def find_index(string, target):
    return string.find(target)

def starts_with(string, prefix):
    return string.startswith(prefix)

def ends_with(string, suffix):
    return string.endswith(suffix)

def is_all_digits(string):
    return string.isdigit()

def to_uppercase(string):
    return string.upper()

def to_lowercase(string):
    return string.lower()

def split_string(string, delimiter):
    return string.split(delimiter)


# Test the functions
if __name__ == "__main__":
    name = "Raghav"

    # Testing the functions
    print(count_occurrences(name, "a"))  
    print(replace_chars(name, "a", "A"))
    print(find_index(name, "a"))  
    print(starts_with(name, "Ra"))  
    print(ends_with(name, "ha"))  
    print(is_all_digits(name))  
    print(to_uppercase(name))  
    print(to_lowercase(name))  
    print(split_string(name, "a"))  
