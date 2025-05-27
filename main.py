def get_book_test(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    path_to_file = "./books/frankenstein.txt"
    text = (get_book_test(path_to_file))
    return text

def word_count(text):
    split_words = text.split()   
    print(len(split_words), "words found in the document")

main()
word_count(main())