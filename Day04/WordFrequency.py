sentence = input("Enter a sentence:\n")

words = sentence.split()

word_counts = {}

for word in words:
    word_lower = word.lower()
    
    if word_lower in word_counts:
        word_counts[word_lower] += 1
    else:
        word_counts[word_lower] = 1

print("\nOutput\n")
for key, value in word_counts.items():
    print(f"{key} : {value}")