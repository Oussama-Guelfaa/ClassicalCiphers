# tests/test_vigenere.py

import unittest
from ciphers.vigenere import VigenereCipher


class TestVigenereCipher(unittest.TestCase):
    def test_encrypt(self):
        cipher = VigenereCipher("KEY")
        self.assertEqual(cipher.encrypt("HELLO"), "RIJVS")

    def test_decrypt(self):
        cipher = VigenereCipher("KEY")
        self.assertEqual(cipher.decrypt("RIJVS"), "HELLO")

    def test_non_alpha(self):
        cipher = VigenereCipher("KEY")
        self.assertEqual(cipher.encrypt("HELLO WORLD!"), "RIJVS UYVJN!")


if __name__ == "__main__":
    unittest.main()
