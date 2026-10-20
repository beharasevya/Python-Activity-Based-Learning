print("RETAIL BILLING")

number_of_items = int(input("How many items? "))
grand_total = 0

for item_number in range(1, number_of_items + 1):
    name = input(f"Enter name of item {item_number}: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: ₹"))

    subtotal = quantity * price
    grand_total += subtotal
    print(f"{name}: {quantity} x ₹{price:.2f} = ₹{subtotal:.2f}")

print("-" * 30)
print(f"Grand Total: ₹{grand_total:.2f}")
