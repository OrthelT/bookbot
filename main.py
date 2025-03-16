def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text

def main():
    book = get_book_text('books/frankenstein.txt')
    return book

def count_words(text):
    words = text.split()
    return len(words)

t = main()
print(f"{count_words(main())} words found in the document")

