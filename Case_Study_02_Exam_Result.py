print("EXAM RESULT")

subjects = int(input("Enter number of subjects: "))
total = 0
all_pass = True

for i in range(1, subjects + 1):
    mark = float(input(f"Enter marks for subject {i} (0-100): "))
    if mark < 0 or mark > 100:
        print("Invalid marks. Enter marks from 0 to 100.")
        raise SystemExit
    total += mark
    if mark < 35:
        all_pass = False

average = total / subjects

if not all_pass:
    grade = "F"
    result = "Fail"
elif average >= 90:
    grade = "A"
    result = "Pass"
elif average >= 75:
    grade = "B"
    result = "Pass"
elif average >= 60:
    grade = "C"
    result = "Pass"
else:
    grade = "D"
    result = "Pass"

print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
print(f"Result: {result}")
