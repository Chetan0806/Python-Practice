sentence = input("Enter a sentence:\n")

words = sentence.split()

longest = ""
second_longest = ""

for word in words:
    word_len = len(word)

    if word_len > len(longest):
        second_longest = longest
        longest = word

    elif word_len > len(second_longest) and word != longest:
        second_longest = word

print(f"\nSecond longest word: {second_longest}")