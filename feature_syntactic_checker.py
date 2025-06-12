import re
from collections import Counter

def word_standardization(word):
    return re.sub(r'[^A-Za-z]', ' ', word.upper())

def is_anagram(word_1, word_2):
    return Counter(word_1) == Counter(word_2)

def overlap_percentage(word_1, word_2):
    common_letters = set(word_1) & set(word_2)
    all_letters = set(word_1) | set(word_2)
    letter_overlap = len(common_letters) / len(all_letters) if all_letters else 0
    return int(round(letter_overlap, 2) * 100)