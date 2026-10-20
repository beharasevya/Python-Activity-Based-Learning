print("PASSWORD VALIDATION")

password = input("Enter a password to check: ")

checks = {
    "At least 8 characters": len(password) >= 8,
    "An uppercase letter": any(ch.isupper() for ch in password),
    "A lowercase letter": any(ch.islower() for ch in password),
    "A digit": any(ch.isdigit() for ch in password),
    "A special character": any(not ch.isalnum() for ch in password),
}

failed = [rule for rule, passed in checks.items() if not passed]

if not failed:
    print("Password meets all sample rules.")
else:
    print("Password does not meet these rules:")
    for rule in failed:
        print("-", rule)
