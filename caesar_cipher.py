# 🛡️ Caesar Cipher – Built with Love & Logic
# Author: B S Namith Kumar
# Internship: SkillCraft Technology (Cybersecurity Track)
# Description: A simple, clean encryption tool to explore classical ciphers, brute-force logic, and the power of Python.

def encrypt_message(message, shift):
    """
    Encrypts a message by shifting each letter forward in the alphabet.
    Keeps punctuation, numbers, and spaces untouched.
    """
    encrypted = ""

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted += shifted_char
        else:
            encrypted += char  # No changes to spaces or symbols

    return encrypted


def decrypt_message(cipher, shift):
    """
    Decrypts a Caesar Cipher by reversing the shift.
    """
    return encrypt_message(cipher, -shift)


def brute_force_attack(cipher):
    """
    Cracks Caesar Cipher without a known key.
    Tries all 25 possibilities – old-school brute force.
    """
    print("\n🔍 Let's try every possible key and see what makes sense:\n")
    for possible_key in range(1, 26):
        guess = decrypt_message(cipher, possible_key)
        print(f"🔑 Key {possible_key:2}: {guess}")
    print("\n👆 Pick the one that looks right to you.")


def show_menu():
    print("\n📜 Caesar Cipher – Cybersecurity Internship Project")
    print("--------------------------------------------------")
    print("1. 🔐 Encrypt a message")
    print("2. 🔓 Decrypt with known key")
    print("3. 🕵️ Brute-force (no key)")
    print("0. 🚪 Exit")


def main():
    print("👋 Hey there, welcome to Caesar Cipher!")
    print("This isn't just code – it's classical cryptography brought to life.")

    while True:
        show_menu()

        try:
            choice = int(input("\n👉 What do you want to do? (0-3): "))

            if choice == 1:
                plain = input("📝 Type your message: ")
                key = int(input("🔑 Enter a key (0–25): "))
                encrypted = encrypt_message(plain, key)
                print(f"\n✅ Encrypted Output: {encrypted}")

            elif choice == 2:
                cipher = input("🔐 Enter the encrypted message: ")
                key = int(input("🔑 Enter the key used: "))
                decrypted = decrypt_message(cipher, key)
                print(f"\n✅ Decrypted Output: {decrypted}")

            elif choice == 3:
                cipher = input("🕵️ Paste the cipher text: ")
                brute_force_attack(cipher)

            elif choice == 0:
                print("👋 Exiting. Stay ethical. Stay curious. Keep hacking the right way.")
                break

            else:
                print("⚠️ Hmm... please enter a number from 0 to 3.")

        except ValueError:
            print("⚠️ Invalid input. Only numbers allowed. Try again!")

if __name__ == "__main__":
    main()
