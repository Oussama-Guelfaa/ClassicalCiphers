# tests/test_playfair.py

import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


import unittest
from ciphers.playfair import PlayfairCipher


class TestPlayfairCipher(unittest.TestCase):
    def test_encrypt(self):
        cipher = PlayfairCipher("KEYWORD")
        self.assertEqual(cipher.encrypt("HELLO"), "GYIZSC")

    def test_decrypt(self):
        cipher = PlayfairCipher("KEYWORD")
        self.assertEqual(cipher.decrypt("DKFVCV"), "REHTAZ")


if __name__ == "__main__":
    unittest.main()
