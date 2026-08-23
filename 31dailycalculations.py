#Program 31: for easy daily life calculations
#Calculate your age
print("To calculate your age")
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print("Your age is:", age)
#Calculate youyr BMI
weight = float(input("To calculate your BMI \n Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height ** 2)
print("Your BMI is:", bmi)
#calculate your bill split
total = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
print("Each person should pay:", total / people)
#Calculate your number of study hours
hours = list(map(float, input("Enter study hours each day separated by space: ").split()))
print("Total study hours:", sum(hours))
print("Average per day:", sum(hours)/len(hours))
#Calculate your currency conversion
rupees = float(input("Enter amount in INR: "))
usd = rupees / 83  # Example rate
print("Equivalent in USD:", usd)

