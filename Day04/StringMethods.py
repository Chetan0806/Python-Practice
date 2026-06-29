sentence = input("Enter a sentence: ")

print("Uppercase:")
print(sentence.upper())

print("Lowercase:")
print(sentence.lower())

print("Title case:")
print(sentence.title())

print("Stripped spaces:")
print(sentence.strip())

old_word = input("Enter the word you want to replace: ")
new_word = input("Enter the new word: ")
print("After replacement:")
print(sentence.replace(old_word, new_word))

char_to_count = input("Enter a character to count: ")
print("Character count:")
print(sentence.count(char_to_count))

start_letter = input("Enter a letter to check if the sentence starts with it: ")
print("Starts with that letter?:")
print(sentence.startswith(start_letter))

end_letter = input("Enter a letter to check if the sentence ends with it: ")
print("Ends with that letter?:")
print(sentence.endswith(end_letter))