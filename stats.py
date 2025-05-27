import sys
def word_count(text):
    split_words = text.split()
    print("============ BOOKBOT ============")
    print("Analyzing book found at", sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found {len(split_words)} total words")

def char_count(text):
    char_qty = {}
    lower_text = list(text.lower())

    for l in lower_text:
        if l in char_qty:
            char_qty[l] = char_qty[l] + 1
        else:
            char_qty[l] = 1
    ##print(char_qty)
    return char_qty

def char_sort(char_qty):
    def sort_on(dict):
        return dict["num"]

    sorted_chars = []
    filtered_sort = []

    for l in char_qty:
        temp_key = {"char": l, "num": char_qty[l]}
        sorted_chars.append(temp_key)

    for c in sorted_chars:
        if c["char"].isalpha():
            filtered_sort.append(c)
    
    filtered_sort.sort(reverse=True, key=sort_on)

    for f in filtered_sort:
        print(f"{f['char']}: {f['num']}")
    print("============= END ===============")
    return filtered_sort