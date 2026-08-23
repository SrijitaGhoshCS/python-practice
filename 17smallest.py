# Program 17: Smallest element in list

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("The smallest element in the list is:", smallest)
