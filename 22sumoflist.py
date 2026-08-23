# Program 22: Sum of list elements
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
total = 0
for num in numbers:
    total += num
print("The sum of list elements is:", total)
