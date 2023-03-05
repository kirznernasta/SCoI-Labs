from help_functioins import count_sentences, calc_average_sentence_length, calc_average_word_length, \
    calculate_top_k_repeated_n_grams
from text_statistics import get_statistics

if __name__ == '__main__':
    # get_statistics('/home/kirznernasta/scoi_test/task_1/file.txt')


    print(calculate_top_k_repeated_n_grams('This is a test file. It contains some text for testing. This is a test file!'))
    print(calculate_top_k_repeated_n_grams(''))
