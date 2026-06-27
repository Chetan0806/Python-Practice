def count_vowels(text):
    vowels = "aeiou"
    vowel_count = 0

    clean_text = text.lower()

    for char in clean_text:
        if char in vowels:
            vowel_count += 1

    return vowel_count


user_string = input("Enter a sentence: ")

total_vowels = count_vowels(user_string)

print(f"The number of vowels in your text is: {total_vowels}")