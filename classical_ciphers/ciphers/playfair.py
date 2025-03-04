# ciphers/playfair.py

import re
from classical_ciphers.ciphers.tests.logging_config import logger


class PlayfairCipher:
    def __init__(self, key):
        logger.info("Initializing PlayfairCipher with key: %s", key)
        self.key = self._generate_key_matrix(key)
        logger.debug("Generated Playfair key matrix: %s", self.key)

    def encrypt(self, plaintext):
        logger.info("Encrypting with PlayfairCipher: %s", plaintext)
        return self._process_text(plaintext, mode="encrypt")

    def decrypt(self, ciphertext):
        logger.info("Decrypting with PlayfairCipher: %s", ciphertext)
        return self._process_text(ciphertext, mode="decrypt")

    def _generate_key_matrix(self, key):
        key = "".join(sorted(set(key.upper()), key=lambda x: key.index(x)))
        key = key.replace("J", "I")
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key_matrix = [char for char in key if char in alphabet]
        key_matrix += [char for char in alphabet if char not in key_matrix]
        return [key_matrix[i : i + 5] for i in range(0, 25, 5)]

    def _process_text(self, text, mode):
        logger.info("Processing text: %s, Mode: %s", text, mode)
        text = text.upper().replace("J", "I")
        text = re.sub(r"[^A-Z]", "", text)
        pairs = self._create_pairs(text)
        logger.debug("Text pairs: %s", pairs)
        processed_text = ""

        for pair in pairs:
            logger.debug("Processing pair: %s", pair)
            pos1 = self._find_position(pair[0])
            pos2 = self._find_position(pair[1])
            logger.debug("Positions: %s, %s", pos1, pos2)

            if pos1[0] == pos2[0]:
                # Same row
                col1 = (pos1[1] + (1 if mode == "encrypt" else -1)) % 5
                col2 = (pos2[1] + (1 if mode == "encrypt" else -1)) % 5
                processed_text += self.key[pos1[0]][col1] + self.key[pos2[0]][col2]
            elif pos1[1] == pos2[1]:
                # Same column
                row1 = (pos1[0] + (1 if mode == "encrypt" else -1)) % 5
                row2 = (pos2[0] + (1 if mode == "encrypt" else -1)) % 5
                processed_text += self.key[row1][pos1[1]] + self.key[row2][pos2[1]]
            else:
                # Rectangle swap
                processed_text += (
                    self.key[pos1[0]][pos2[1]] + self.key[pos2[0]][pos1[1]]
                )
            logger.debug("Intermediate processed text: %s", processed_text)

        logger.info("Final processed text: %s", processed_text)
        return processed_text

    def _create_pairs(self, text):
        pairs = []
        i = 0
        while i < len(text):
            a = text[i]
            b = ""
            if i + 1 < len(text):
                b = text[i + 1]
            if a != b:
                pairs.append(a + (b if b else "X"))
                i += 2
            else:
                pairs.append(a + "X")
                i += 1
        if len(pairs[-1]) == 1:
            pairs[-1] += "X"
        return pairs

    def _find_position(self, char):
        for row_idx, row in enumerate(self.key):
            if char in row:
                return (row_idx, row.index(char))
        raise ValueError(f"Character {char} not found in key matrix.")
