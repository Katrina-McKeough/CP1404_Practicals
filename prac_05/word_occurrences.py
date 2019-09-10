text = input("Text: ")
words = text.split(" ")
max_length = max(len(word) for word in words)
word_occurrences = {}
for word in words:
    word_occurrences[word] = word_occurrences.get(word, 0) + 1
words = list(word_occurrences.keys())
words.sort()
for word in words:
    print("{:{}s} : {}".format(word, max_length, word_occurrences[word]))
