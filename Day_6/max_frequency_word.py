def max_frequency_word(text):
    # Convert text to lowercase and split into words
    words = text.lower().split()
    
    # Count frequency of each word
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    # Find the word with the maximum frequency
    max_freq = max(frequency.values())
    max_freq_words = [word for word, freq in frequency.items() if freq == max_freq]
    
    # If multiple words have the same frequency, choose the one with maximum length
    max_freq_words.sort(key=lambda x: len(x), reverse=True)
    
    return f"{max_freq_words[0]} {max_freq}"

# Test cases
text1 = "Work like you do not need money love like you have never been hurt and dance like no one is watching"
text2 = "Courage is not the absence of fear but rather the judgement that something else is more important than fear"

print(max_frequency_word(text1))
print(max_frequency_word(text2))
