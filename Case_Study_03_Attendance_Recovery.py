print("ATTENDANCE RECOVERY")

attended = int(input("Classes attended: "))
total = int(input("Total classes held: "))
target = float(input("Target attendance percentage: "))

if total <= 0 or attended < 0 or attended > total or not (0 < target <= 100):
    print("Please enter valid values.")
    raise SystemExit

current = attended / total * 100
extra = 0

while current < target:
    attended += 1
    total += 1
    extra += 1
    current = attended / total * 100

print(f"Current attendance: {attended - extra}/{total - extra}")
print(f"Classes to attend continuously: {extra}")
print(f"Attendance after recovery: {current:.2f}%")
