print("REPEATED TRANSACTIONS")

count = int(input("Number of transactions: "))
transactions = []

for i in range(1, count + 1):
    amount = float(input(f"Transaction {i} amount: ₹"))
    transactions.append(amount)

frequency = {}
for amount in transactions:
    frequency[amount] = frequency.get(amount, 0) + 1

repeated = [amount for amount, times in frequency.items() if times > 1]

if repeated:
    print("Repeated amounts:", ", ".join(f"₹{x:.2f}" for x in repeated))
else:
    print("No repeated transaction amounts.")
