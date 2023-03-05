import os

from help_functioins import count_sentences, count_non_declarative, calc_average_sentence_length, \
    calc_average_word_length, calculate_top_k_repeated_n_grams


def get_input(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            return get_statistics(file.read())
    else:
        return f'File {filepath} is not found.'


def get_statistics(input_text: str, k=10, n=4):
    if os.path.exists(input_text):
        with open(input_text, "r") as file:
            print(f'From a file {input_text}:')
            return get_statistics(file.read())
    else:

        print(f'Text:\n{input_text}\n\nStatistics:\n'
              f'Amount of sentences: {count_sentences(input_text)}\n'
              f'Amount of non-declarative sentences: {count_non_declarative(input_text)}\n'
              f'Average length of the sentence in characters: {calc_average_sentence_length(input_text)}\n'
              f'Average length of the word: {calc_average_word_length(input_text)}\n'
              f'top-{k} repeated {n}-grams: \n {calculate_top_k_repeated_n_grams(input_text, k, n)}')
