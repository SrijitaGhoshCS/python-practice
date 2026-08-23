# Program 27: Compound Interest Calculator
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time (in years): "))
n = int(input("Enter number of times interest applied per year: "))
amount = principal * (1 + (rate / (100 * n)))**(n * time)
CI = amount - principal
print("Compound Interest =", CI)
print("Total Amount =", amount)

#Program in one-liner
P = float(input("Enter principal: "))
R = float(input("Enter rate (%): "))
T = float(input("Enter time (years): "))
A = P * (1 + R/100)**T
CI = A - P
print("Compound Interest =", CI)

