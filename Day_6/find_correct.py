def find_correct(words):
    correct = 0
    almost_correct = 0
    wrong = 0
    
    for key, value in words.items():
        if key == value:
            correct += 1
        elif len(key) == len(value):
            count_diff = sum(1 for a, b in zip(key, value) if a != b)
            if count_diff <= 2:
                almost_correct += 1
            else:
                wrong += 1
        else:
            wrong += 1
    
    return [correct, almost_correct, wrong]

# Test case
words = {"THEIR": "THEIR", "BUSINESS": "BISINESS", "WINDOWS": "WINDMILL", "WERE": "WEAR", "SAMPLE": "SAMPLE"}
print(find_correct(words))  # Output: [2, 2, 1]
