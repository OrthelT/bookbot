import sys
from stats import get_num_words, get_chars

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file = sys.argv[1]
    book = get_book_text(book_file)
    words = get_num_words(book) 
    message = f"Found {words} total words"
    dict_list = get_chars(book)
    make_report(book_file,dict_list,message)

def show_counts(dict_list):
    for d in dict_list:
        for k, v in d.items():
            print(f"{k}: {v}")

def make_report(book_file,dict_list, message):
    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {book_file}...
  
    ----------- Word Count ----------
    {message}
    --------- Character Count -------
          """)
    show_counts(dict_list)
    print('============= END ===============')

main()

