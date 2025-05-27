from stats import word_count, char_count, char_sort

def get_book_test(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    path_to_file = "./books/frankenstein.txt"
    text = (get_book_test(path_to_file))
    return text

text = main()
word_count(text)
char_counts = char_count(text)
sorted_counts = char_sort(char_counts)