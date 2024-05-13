
def book_text(path):
    with open(path) as f:
        return f.read()
    
def word_leng(string):
    words = string.split()
    return(len(words))

def letter_count(text):
    letter = {}
    for l in text:
        new_text = l.lower()
        if new_text in letter:
            letter[new_text] +=1
        else:
            letter[new_text] = 1
    return letter

def sort_on(d):
    return d["num"]

def char_dict_to_sorted_list(chars_dict):
    sort_list = []
    for ch in chars_dict:
        sort_list.append({"char": ch,"num": chars_dict[ch]})
    sort_list.sort(reverse=True,key=sort_on)
    return sort_list


def main():
    path = "books/frankenstein.txt"
    text = book_text(path)
    text_leng = word_leng(text)
   
    letters_counts = letter_count(text)
    sorted_char_list = (char_dict_to_sorted_list(letters_counts))
    print(f"--- Begin report of {path} ---")
    print(f"{text_leng} words found in the document")
    print()

    for item in sorted_char_list:
        if not item["char"].isalpha():
            continue
        print(f"the '{item['char']}' character was found {item['num']}' times ")

    print("--- End report ---")

    

main()
                

