print("NUMERIC PATTERN")

rows = int(input("Enter number of rows: "))
if rows <= 0:
    print("Enter a positive number.")
    raise SystemExit

for row in range(1, rows + 1):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()
