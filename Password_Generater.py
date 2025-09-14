import random
import string

def generate_password():
    # Character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*?%"

    # Password length: 12–16
    length = random.randint(12, 16)

    # Mandatory characters
    password = [
        random.choice(uppercase), random.choice(uppercase),  # 2 uppercase
        random.choice(digits), random.choice(digits),        # 2 digits
        random.choice(special), random.choice(special)       # 2 special
    ]

    # Fill remaining slots with random characters from all groups
    all_chars = uppercase + lowercase + digits + special
    remaining = length - len(password)
    password += random.choices(all_chars, k=remaining)

    # Shuffle for randomness
    random.shuffle(password)

    return ''.join(password)

# Main loop
while True:
    pwd = generate_password()
    print(f"\nGenerated Strong Password: {pwd}")

    choice = input("Do you want a new password? (yes/no): ").strip().lower()
    if choice != "yes":
        print("Exiting... Stay safe with unique strong passwords! 🔐")
        break

