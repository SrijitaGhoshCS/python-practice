# Program 11: Armstrong number check
num = int(input("Enter a number: "))
sum_of_powers = 0
digits = len(str(num))
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** digits
    temp