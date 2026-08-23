# Program: Voting Eligibility Checker

age = int(input("Enter your age: "))
citizen = input("Are you an Indian citizen? (yes/no): ").lower()

if age >= 18 and citizen == "yes":
    print("✅ You are eligible to vote in India.")
else:
    print("❌ You are not eligible to vote.")
