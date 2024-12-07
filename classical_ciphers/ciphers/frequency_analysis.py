# utils/frequency_analysis.py

from collections import Counter


class FrequencyAnalysis:
    @staticmethod
    def analyze(text):
        text = "".join(filter(str.isalpha, text.upper()))
        total_chars = len(text)
        frequencies = Counter(text)
        frequency_percentages = {
            char: (count / total_chars) * 100 for char, count in frequencies.items()
        }
        return frequency_percentages
