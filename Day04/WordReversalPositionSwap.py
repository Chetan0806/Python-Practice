sentence = input("Enter a sentence: ")
words = sentence.split()

reversed_words = words[::-1]

output_sentence = " ".join(reversed_words)

print(output_sentence)