# Program 9: Palindrome check
text = input("Enter a string: ")
reversed_text = text[::-1]
if text == reversed_text:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")
