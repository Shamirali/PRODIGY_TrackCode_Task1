#!/usr/bin/env python3

def encrypt_caesar(text: str, shift: int) -> str:
    """Encrypt text using Caesar Cipher."""
    result = ""
    shift = shift % 26  # Handle large shift values

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep symbols and spaces unchanged

    return result


def decrypt_caesar(text: str, shift: int) -> str:
    """Decrypt text using Caesar Cipher."""
    return encrypt_caesar(text, -shift)


def brute_force(text: str):
    """Try all possible shifts (for learning purpose)."""
    print("\n🔎 Brute Force Results:")
    for shift in range(26):
        print(f"Shift {shift:2}: {decrypt_caesar(text, shift)}")


def get_shift_value() -> int:
    """Safely get integer shift value from user."""
    while True:
        try:
            shift = int(input("Enter shift value: "))
            return shift
        except ValueError:
            print("❌ Please enter a valid number.")


def main():
    while True:
        print("\n===== Caesar Cipher Tool =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Brute Force Attack")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            message = input("Enter message to encrypt: ")
            shift = get_shift_value()
            encrypted = encrypt_caesar(message, shift)
            print(f"\n✅ Encrypted Message: {encrypted}")

        elif choice == "2":
            message = input("Enter message to decrypt: ")
            shift = get_shift_value()
            decrypted = decrypt_caesar(message, shift)
            print(f"\n✅ Decrypted Message: {decrypted}")

        elif choice == "3":
            message = input("Enter message for brute force: ")
            brute_force(message)

        elif choice == "4":
            print("👋 Exiting program. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
