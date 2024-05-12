#def main():
#    with open("books/frankenstein.txt") as f:
#        text = f.read()
#        print(text)

# Course instructor's solution:
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    print(word_count(text))


def get_book_text(path):
    with open(path) as f:
        return f.read()

# Add a new function to your script that takes the text from the book as a string, and returns the number of words in the string.
def word_count(text):
    words = text.split()
    return len(words)

main()