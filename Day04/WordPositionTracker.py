sentence = input("Enter a sentence: ")

words = sentence.split()

for index, word in enumerate(words, start=1):
    print(f"{word} -> {index}")