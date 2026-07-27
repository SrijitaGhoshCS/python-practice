# Program to check if a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
elif num % 2 != 0:
    print(num, "is Odd")
else:
    print(num, "is neither even nor odd")
