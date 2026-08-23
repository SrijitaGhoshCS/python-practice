# Program: Pass/Fail Rate of Students
#!:Take number of students
n = int(input("Enter total number of students: "))

# Step 2: Initialize counters
pass_count = 0
fail_count = 0

# Step 3: Loop through each student
for i in range(n):
    marks = float(input(f"Enter marks of student {i+1}: "))
    if marks >= 40:   # Assuming 40 is the pass mark
        pass_count += 1
    else:
        fail_count += 1

# Step 4: Calculate percentages
pass_rate = (pass_count / n) * 100
fail_rate = (fail_count / n) * 100

# Step 5: Print results
print("Number of students passed:", pass_count)
print("Number of students failed:", fail_count)
print("Pass rate:", pass_rate, "%")
print("Fail rate:", fail_rate, "%")
