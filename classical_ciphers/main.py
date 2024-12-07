# main.py

from ciphers.caesar import CaesarCipher
from ciphers.vigenere import VigenereCipher
from ciphers.playfair import PlayfairCipher
from utils.frequency_analysis import FrequencyAnalysis


def main():
    print("Classical Ciphers Program")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")
    print("3. Playfair Cipher")
    choice = input("Select a cipher (1-3): ").strip()

    if choice == "1":
        key = int(input("Enter the key (1-25): "))
        cipher = CaesarCipher(key)
    elif choice == "2":
        key = input("Enter the key (alphabetic characters only): ")
        cipher = VigenereCipher(key)
    elif choice == "3":
        key = input("Enter the key (alphabetic characters only): ")
        cipher = PlayfairCipher(key)
    else:
        print("Invalid choice!")
        return

    mode = (
        input("Do you want to (E)ncrypt, (D)ecrypt, or (A)nalyze frequency? ")
        .strip()
        .upper()
    )
    text = input("Enter your message: ")

    if mode == "E":
        result = cipher.encrypt(text)
        print("Encrypted message:", result)
    elif mode == "D":
        result = cipher.decrypt(text)
        print("Decrypted message:", result)
    elif mode == "A":
        frequencies = FrequencyAnalysis.analyze(text)
        print("Frequency Analysis:")
        for char, freq in sorted(frequencies.items()):
            print(f"{char}: {freq:.2f}%")
    else:
        print("Invalid mode!")


if __name__ == "__main__":
    main()
