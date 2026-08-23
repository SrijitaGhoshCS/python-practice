# Program 26: Simple Interest Calculator
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (per year in %): "))
time = float(input("Enter the time (in years): "))
SI = (principal * rate * time) / 100
print("Simple Interest =", SI)
print("Amount=",principal+SI)
