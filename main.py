from stats import word_count, char_count

def get_book_test(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    path_to_file = "./books/frankenstein.txt"
    text = (get_book_test(path_to_file))
    return text

word_count(main())
char_count(main())