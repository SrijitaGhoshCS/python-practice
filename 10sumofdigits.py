# Program 10: Sum of digits
num = int(input("Enter a number: "))
digit_sum = 0
while num > 0:
    digit = num % 10        
    digit_sum += digit      
    num = num // 10         

# Step 4: Print the result
print("Sum of digits is:", digit_sum)
print('hello')
