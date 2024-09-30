def word_count(book):
    return len(book.split())

def char_count(book):
    char_dict = {}
    char_list = []
    lower_case_book = book.lower()
    for char in lower_case_book:
        if char in char_dict and char.isalpha():
            char_dict[char] += 1
        elif char.isalpha() and char not in char_dict:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]       

def main():
    with open("books/frankenstein.txt") as f:
        fran_book = f.read()

    w_count = word_count(fran_book)
    c_dict = char_count(fran_book)
    char_list = [{"char":k, "count":c_dict[k]} for k in c_dict]
    char_list.sort(reverse = True, key=sort_on)
    
    
    
    print("--- Begin report of books/Frankenstein.txt ---")
    print(f"{w_count} words found in the document")
    for c in char_list:
        print(f"The {c['char']} character was found {c['count']} times")
    print("--- End Report ---")
    

main()