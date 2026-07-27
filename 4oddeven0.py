# Program to check if a number is even or odd, excluding 0

num = int(input("Enter a number: "))

if num == 0:
    print("Zero is neither even nor odd")
elif num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
