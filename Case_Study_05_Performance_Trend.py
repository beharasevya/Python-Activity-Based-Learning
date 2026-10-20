print("PERFORMANCE TREND")

count = int(input("Number of tests: "))
if count <= 0:
    print("Enter at least one test.")
    raise SystemExit

marks = []
for i in range(1, count + 1):
    mark = float(input(f"Marks in test {i}: "))
    marks.append(mark)

average = sum(marks) / len(marks)

if marks[-1] > marks[0]:
    trend = "Improving"
elif marks[-1] < marks[0]:
    trend = "Decreasing"
else:
    trend = "Unchanged"

print(f"Average marks: {average:.2f}")
print(f"Performance trend: {trend}")
