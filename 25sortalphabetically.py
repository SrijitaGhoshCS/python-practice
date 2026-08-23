# Program 25: Sort words alphabetically— just like a teacher arranges students’ roll numbers according to names.
words = input("Enter words separated by space: ").split()
words.sort()
print("Words in alphabetical order:")
for word in words:
    print(word)
