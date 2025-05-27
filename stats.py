def word_count(text):
    split_words = text.split()   
    print(len(split_words), "words found in the document")

def char_count(text):
    char_qty = {}
    lower_text = list(text.lower())
    for l in lower_text:
        if l in char_qty:
            char_qty[l] = char_qty[l] + 1
        else:
            char_qty[l] = 1
    print(char_qty)