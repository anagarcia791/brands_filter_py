import re
from difflib import SequenceMatcher


def get_phonetic_features(word):
    features = {
        'starts_with_vowel': word[0] in 'AEIOU' if word else False,
        'ends_with_consonant': word[-1] not in 'AEIOU' if word else False,
        'has_double_letters': any(word[i] == word[i + 1] for i in range(len(word) - 1)),
        'consonant_clusters': len(re.findall(r'[BCDFGHJKLMNPQRSTVWXYZ]{2,}', word)),
        'vowel_pattern': re.sub(r'[BCDFGHJKLMNPQRSTVWXYZ]', 'C', re.sub(r'[AEIOU]', 'V', word))
    }
    return features


def get_phonetic_similarity(word_1, word_2):
    features1 = get_phonetic_features(word_1)
    features2 = get_phonetic_features(word_2)
    phonetic_matches = sum(1 for key in features1 if features1[key] == features2[key])
    return phonetic_matches / len(features1)


def get_string_similarity(word_1, word_2):
    return SequenceMatcher(None, word_1, word_2).ratio()


sound_patterns = {
    'C': 'K', 'K': 'C', 'S': 'Z', 'Z': 'S',
    'F': 'PH', 'PH': 'F', 'TH': 'T'
}


def normalize_sounds(word):
    for original, replacement in sound_patterns.items():
        word = word.replace(original, replacement)
    return word


def get_sound_similarity(word_1, word_2):
    sound_normalized_1 = normalize_sounds(word_1)
    sound_normalized_2 = normalize_sounds(word_2)
    return SequenceMatcher(None, sound_normalized_1, sound_normalized_2).ratio()


def get_total_phonetic_score(word_1, word_2):
    return round((
                         get_phonetic_similarity(word_1, word_2) +
                         get_string_similarity(word_1,word_2) +
                         get_sound_similarity(word_1,word_2)) / 3,2) * 100
