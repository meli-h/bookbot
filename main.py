from stats import count_words, count_characters,sort_characters
import sys


HEADER  = "============ BOOKBOT ============"
FOOTER  = "============= END ==============="
WC_LINE = "----------- Word Count ----------"
CC_LINE = "--------- Character Count -------"

def main():
    print("Usage: python3 main.py <path_to_book>")
    if len(sys.argv) > 1:
        BOOKPATH = sys.argv[1]
    else:
        sys.exit(1)

    file_path = BOOKPATH 

    content = (get_book_test(file_path))

    num_words = count_words(content)
    
    d = count_characters(content)

    print(HEADER)
    print("Analyzing book found at books/frankenstein.txt...")

    print(WC_LINE)
    print(f"Found {num_words} total words")
    print(CC_LINE)
    for each in sort_characters(d):
        print(f"{each[0]}: {each[1]}")

    print(FOOTER)
    
    

def get_book_test (filep):
    with open(filep) as file:
        content = file.read()
    return content


if __name__ == "__main__":
    main()



    