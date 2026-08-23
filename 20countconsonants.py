# Program: Count vowels and consonants in a string

text = input("Enter a string: ")

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in text.lower():
    if char.isalpha():   # Only check letters
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
