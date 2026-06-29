sentence = input("Enter a sentence: ")

spaces = 0
vowels = 0
consonants = 0

all_vowels = "aeiou"

for char in sentence:
    char_lower = char.lower()
    
    if char == " ":
        spaces += 1
    elif char_lower in all_vowels:
        vowels += 1
    elif char_lower.isalpha():
        consonants += 1
        

total_characters = len(sentence)

print(f"Total characters: {total_characters}")
print(f"Spaces: {spaces}")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")