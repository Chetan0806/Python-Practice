word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

word1_clean = word1.lower()
word2_clean = word2.lower()

if sorted(word1_clean) == sorted(word2_clean):
    print("\nThe words are anagrams.")
else:
    print("\nThe words are not anagrams.")