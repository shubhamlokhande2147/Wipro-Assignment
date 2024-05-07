def Test(message):
    words = message.split()
    encrypted_message = []
    for i, word in enumerate(words, 1):
        if i % 2 != 0:
            encrypted_message.append(word[::-1])
        else:
            consonants = ''.join([c for c in word if c.lower() not in 'aeiou'])
            vowels = ''.join([c for c in word if c.lower() in 'aeiou'])
            encrypted_message.append(consonants + vowels)
    return ' '.join(encrypted_message)

# Test the function
print(Test("the sun rises"))  
print(Test("in the east")) 
