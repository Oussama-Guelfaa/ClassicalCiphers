# tests/test_playfair.py

import unittest
from ciphers.playfair import PlayfairCipher


class TestPlayfairCipher(unittest.TestCase):
    def test_encrypt(self):
        cipher = PlayfairCipher("KEYWORD")
        self.assertEqual(cipher.encrypt("HELLO"), "DKFVCV")

    def test_decrypt(self):
        cipher = PlayfairCipher("KEYWORD")
        self.assertEqual(cipher.decrypt("DKFVCV"), "HELXLO")


if __name__ == "__main__":
    unittest.main()
