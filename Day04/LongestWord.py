sentence = input("Enter a sentence: ")

words = sentence.split()

longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"Longest word: {longest_word}")
print(f"Length: {len(longest_word)}")