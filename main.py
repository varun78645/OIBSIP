
import string
import secrets

print("==============================")
print("   RANDOM PASSWORD GENERATOR")
print("==============================")

try:
    length = int(input("Enter password length (minimum 8): "))

    if length < 8:
        print("Error: Password must be at least 8 characters long.")

    else:
        # Create character groups
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        numbers = string.digits
        special = string.punctuation

        # Ensure at least one character from each group
        password = [
            secrets.choice(lowercase),
            secrets.choice(uppercase),
            secrets.choice(numbers),
            secrets.choice(special)
        ]

        # Add remaining random characters
        all_characters = lowercase + uppercase + numbers + special

        for i in range(length - 4):
            password.append(secrets.choice(all_characters))

        # Shuffle the password
        secrets.SystemRandom().shuffle(password)

        # Display password
        final_password = "".join(password)

        print("\nYour generated password is:")
        print(final_password)

except ValueError:
    print("Error: Please enter a valid number.")
