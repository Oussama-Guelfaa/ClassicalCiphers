# tests/test_caesar.py

import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


import unittest
from ciphers.caesar import CaesarCipher


class TestCaesarCipher(unittest.TestCase):
    def test_encrypt(self):
        cipher = CaesarCipher(3)
        self.assertEqual(cipher.encrypt("HELLO"), "KHOOR")

    def test_decrypt(self):
        cipher = CaesarCipher(3)
        self.assertEqual(cipher.decrypt("KHOOR"), "HELLO")

    def test_non_alpha(self):
        cipher = CaesarCipher(3)
        self.assertEqual(cipher.encrypt("HELLO WORLD!"), "KHOOR ZRUOG!")


if __name__ == "__main__":
    unittest.main()
