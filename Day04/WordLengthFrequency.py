sentence = input("Enter a sentence: ")
words = sentence.split()

freq = {}

for word in words:
    length = len(word)

    if length in freq:
        freq[length] += 1
    else:
        freq[length] = 1

for length in sorted(freq):
    print(f"{length}-letter words: {freq[length]}")