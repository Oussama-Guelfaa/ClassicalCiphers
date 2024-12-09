# main.py


from logging_config import logger
from caesar import CaesarCipher
from vigenere import VigenereCipher
from playfair import PlayfairCipher
from frequency_analysis import FrequencyAnalysis


def main():
    logger.info("Starting Classical Ciphers Program")
    print("*" * 40)
    print("*" + " " * 38 + "*")
    print("*" + " Classical Ciphers Program".center(38) + "*")
    print("*" + " " * 38 + "*")
    print("*" * 40)
    print("\nChoose a Cipher:")
    print("★ 1. Caesar Cipher")
    print("★ 2. Vigenère Cipher")
    print("★ 3. Playfair Cipher")
    print("\n" + "*" * 40)

    choice = input("Select a cipher (1-3): ").strip()

    try:
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
            logger.warning("Invalid cipher choice: %s", choice)
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
            logger.info("Encryption result: %s", result)
            print("Encrypted message:", result)
        elif mode == "D":
            result = cipher.decrypt(text)
            logger.info("Decryption result: %s", result)
            print("Decrypted message:", result)
        elif mode == "A":
            frequencies = FrequencyAnalysis.analyze(text)
            logger.info("Frequency Analysis result: %s", frequencies)
            print("Frequency Analysis:")
            for char, freq in sorted(frequencies.items()):
                print(f"{char}: {freq: .2f}%")
        else:
            logger.warning("Invalid mode selected: %s", mode)
            print("Invalid mode!")
    except ValueError as e:
        logger.error("An error occurred: %s", e)
        print(f"Error: {e}")
    except Exception as e:
        logger.critical("Fatal error occurred: %s", e)
        print(f"Fatal Error: {e}")


if __name__ == "__main__":
    main()
