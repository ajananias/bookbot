from stats import get_words, get_characters, sort_characters
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]
        book_text = get_book_text(path_to_file)
        num_words = get_words(book_text)
        characters = get_characters(book_text)
        sorted_list = sort_characters(characters)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in sorted_list:
            print(f"{item["char"]}: {item["num"]}") 

        print("============= END ===============")   

main()