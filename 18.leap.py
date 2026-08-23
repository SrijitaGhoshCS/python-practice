# Program 18: Leap Year Check
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

#Program in one line
year = int(input("Enter a year: "))
print("Leap Year" if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0) else "Not a Leap Year")

