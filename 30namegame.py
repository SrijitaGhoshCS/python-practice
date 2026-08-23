#Program 30: play with your name
# Reverse your Name
name = input("Enter your name: ")
print("Reversed name:", name[::-1])
#count number of letters in your name
fullname=input("enter your full name:")
count=sum(1 for ch in name if ch.isalpha())
print("Number of letters in your name:", count)
#Count vowels in your name
count = sum(1 for ch in name.lower() if ch in "aeiou")
print("Number of vowels in your name:", count)
#Check if your name is palindrome
name = input("Enter your name: ")
if name.lower() == name[::-1].lower():
    print("Your name is a palindrome!")
else:
    print("Not a palindrome.")
#Sort your first and last name alphabetically
names = input("Enter first and last names separated by space: ").split()
names.sort()
print("Names in alphabetical order:", names)
#Nickname Generator
print("so, your nickname could be:", name[:3])
