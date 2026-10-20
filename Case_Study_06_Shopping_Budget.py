print("SHOPPING BUDGET")

budget = float(input("Enter your budget: ₹"))
count = int(input("Number of items: "))
total = 0.0

for i in range(1, count + 1):
    cost = float(input(f"Cost of item {i}: ₹"))
    if cost < 0:
        print("Cost cannot be negative.")
        raise SystemExit
    total += cost

print(f"Shopping total: ₹{total:.2f}")
if total <= budget:
    print(f"Within budget. Money left: ₹{budget - total:.2f}")
else:
    print(f"Over budget by: ₹{total - budget:.2f}")
