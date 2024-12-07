# ciphers/vigenere.py


class VigenereCipher:
    def __init__(self, key):
        if not key.isalpha():
            raise ValueError("Key must consist of alphabetic characters only.")
        self.key = key.upper()

    def encrypt(self, plaintext):
        return self._transform(plaintext, mode="encrypt")

    def decrypt(self, ciphertext):
        return self._transform(ciphertext, mode="decrypt")

    def _transform(self, text, mode):
        result = ""
        key_length = len(self.key)
        key_indices = [ord(char) - ord("A") for char in self.key]
        i = 0

        for char in text:
            if char.isalpha():
                shift = key_indices[i % key_length]
                shift = shift if mode == "encrypt" else -shift
                base = ord("A") if char.isupper() else ord("a")
                shifted = ((ord(char) - base + shift) % 26) + base
                result += chr(shifted)
                i += 1
            else:
                result += char

        return result
