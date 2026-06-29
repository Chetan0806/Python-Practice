word = input("Enter a word: ")

result = ""

for char in word:
    if char not in result:
        result += char

print(result)