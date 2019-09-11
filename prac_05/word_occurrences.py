text = input("Text: ")
words = text.split(" ")
max_length = max(len(word) for word in words)
words_to_occurrences = {}
for word in words:
    words_to_occurrences[word] = words_to_occurrences.get(word, 0) + 1
words = list(words_to_occurrences.keys())
words.sort()
for word in words:
    print("{:{}s} : {}".format(word, max_length, words_to_occurrences[word]))
