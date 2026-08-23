# Program 6: Factorial using loop
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("Factorial of", num, "is:", factorial)
