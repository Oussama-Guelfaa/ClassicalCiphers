# ciphers/caesar.py

class CaesarCipher:
    def __init__(self, key):
        if not isinstance(key, int) or not (1 <= key <= 25):
            raise ValueError("Key must be an integer between 1 and 25.")
        self.key = key

    def encrypt(self, plaintext):
        return self._shift_text(plaintext, self.key)

    def decrypt(self, ciphertext):
        return self._shift_text(ciphertext, -self.key)

    def _shift_text(self, text, shift):
        result = ""

        for char in text:
            if char.isupper():
                shifted = ((ord(char) - ord('A') + shift) % 26) + ord('A')
                result += chr(shifted)
            elif char.islower():
                shifted = ((ord(char) - ord('a') + shift) % 26) + ord('a')
                result += chr(shifted)
            else:
                result += char

        return result