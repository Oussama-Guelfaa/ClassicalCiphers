# ciphers/caesar.py


from logging_config import logger


class CaesarCipher:
    def __init__(self, key):
        if not isinstance(key, int) or not (1 <= key <= 25):
            logger.error("Invalid key: %s (must be an integer between 1 and 25)", key)
            raise ValueError("Key must be an integer between 1 and 25.")
        self.key = key
        logger.info("Initialized CaesarCipher with key: %d", key)

    def encrypt(self, plaintext):
        logger.info("Encrypting with CaesarCipher: %s", plaintext)
        return self._shift_text(plaintext, self.key)

    def decrypt(self, ciphertext):
        logger.info("Decrypting with CaesarCipher: %s", ciphertext)
        return self._shift_text(ciphertext, -self.key)

    def _shift_text(self, text, shift):
        logger.debug("Trace :Shifting text: %s with shift: %d", text, shift)
        result = ""

        for char in text:
            if char.isupper():
                shifted = ((ord(char) - ord("A") + shift) % 26) + ord("A")
                result += chr(shifted)
            elif char.islower():
                shifted = ((ord(char) - ord("a") + shift) % 26) + ord("a")
                result += chr(shifted)
            else:
                result += char

        logger.debug("Trace : Shifted text result: %s", result)
        return result
