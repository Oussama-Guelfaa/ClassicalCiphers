import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import doctest
import ciphers.caesar
import ciphers.playfair
import ciphers.vigenere


doctest.testmod(ciphers.caesar)
doctest.testmod(ciphers.playfair)
doctest.testmod(ciphers.vigenere)
