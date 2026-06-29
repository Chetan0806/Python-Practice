sentence = input("Enter a sentence:\n")

sentence_lower = sentence.lower()

char_counts = {}

for char in sentence_lower:
    # Rule: Ignore spaces
    if char != " ":
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

for key, value in char_counts.items():
    print(f"{key} : {value}")