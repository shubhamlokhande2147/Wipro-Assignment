sentence = "Work like you do not need money love like you have never been hurt and dance like no one is watching"
wordList = sentence.split()

d = {}
for word in wordList:
    d[word] = d.get(word, 0) + 1

max_freq = max(d.values())
max_freq_words = [word for word, freq in d.items() if freq == max_freq]
max_freq_words.sort(key=lambda x: len(x), reverse=True)

print(f"{max_freq_words[0]} {max_freq}")
