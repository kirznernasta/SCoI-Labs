import re

from constants import SENTENCE_PATTERN, NON_DECLARATIVE_PATTERN, WORD_PATTERN, NUMBER_PATTERN, ONE_WORD_ABBREVIATIONS, \
    TWO_WORDS_ABBREVIATIONS, THREE_WORDS_ABBREVIATIONS


def count_sentences(text: str):
    amount = len(re.findall(SENTENCE_PATTERN, text))

    for abbreviation in ONE_WORD_ABBREVIATIONS:
        amount -= text.lower().count(abbreviation)

    for abbreviation in TWO_WORDS_ABBREVIATIONS:
        amount -= text.lower().count(abbreviation) * 2

    for abbreviation in THREE_WORDS_ABBREVIATIONS:
        amount -= text.lower().count(abbreviation) * 3

    return amount if amount >= 0 else 0


def count_non_declarative(text: str):
    return len(re.findall(NON_DECLARATIVE_PATTERN, text))


def calc_average_sentence_length(text: str):
    words = [word for word in re.findall(WORD_PATTERN, text) if word not in re.findall(NUMBER_PATTERN, text)]
    words_len = sum(len(word) for word in words)
    return round(words_len / count_sentences(text), 2) if count_sentences(text) != 0 else 0


def calc_average_word_length(text: str):
    words = re.findall(WORD_PATTERN, text)
    words_len_in_characters = sum(len(word) for word in words)
    return round(words_len_in_characters / len(words), 2) if len(words) != 0 else 0


def calculate_top_k_repeated_n_grams(text: str, k=10, n=4):
    words = re.findall(WORD_PATTERN, text)

    if n > len(words):
        return f'n ({n}) is bigger than amount of words ({len(words)}) in this text!'

    dictionary = {}
    for i in range(len(words) - n + 1):
        n_gram = ' '.join([str(word) for word in words[i:i+n]])
        if n_gram not in dictionary:
            dictionary[n_gram] = 1
        else:
            dictionary[n_gram] += 1

    if len(dictionary) <= k:
        return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[0:k]
