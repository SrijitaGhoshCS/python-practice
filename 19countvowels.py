# Program 19: Count vowels in a string
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels in the string:", count)
#Program in one line
text = input("Enter a string: ")
count = sum(1 for char in text if char.lower() in "aeiou")
print("Number of vowels in the string:", count)
