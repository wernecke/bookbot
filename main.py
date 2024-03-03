def main():
    book_path = "books/frankenstein.txt"
    text = get_book_contents(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words in the document")
    char_dict = get_character_count(text)
    sort_char_dict(char_dict)
    

# def print_char_dict(chars):

def get_num_words(text):
    '''Returns the number of words in a string of text'''
    words = text.split() 
    return len(words) 

def get_book_contents(path):
    with open(path) as f: 
        return f.read()

def sort_char_dict(chars):
    sorted_dict = sorted(chars.items(), key=lambda x: x[1], reverse=True)
    for c, count in sorted_dict:
        print(f"The '{c}' character was found {count} times")
        
def get_character_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

main()
