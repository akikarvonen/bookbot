#def main():
#    with open("books/frankenstein.txt") as f:
#        text = f.read()
#        print(text)

# Course instructor's solution:
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()