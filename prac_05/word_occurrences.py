text = input("Text: ")
words = text.split(" ")
word_occurrences = {}
for word in words:
    word_occurrences[word] = word_occurrences.get(word, 0) + 1
