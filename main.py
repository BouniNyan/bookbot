import sys

if len(sys.argv)!=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_num_words
from stats import get_num_characters
from stats import sort_dict


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book=get_book_text(f"{sys.argv[1]}")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    print("--------- Character Count -------")
    for item in sort_dict(get_num_characters(book)):
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
main()
