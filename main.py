#!/usr/bin/env python3
import sys
import stats
def get_book_text(file_path: str, ) -> str:
    with open(file_path, 'r') as f:
        file_contents = f.read()
        return file_contents
    




def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    print(f"{stats.get_num_words(file_contents)} words found in the document")

    print(stats.count_num_characters(file_contents))

    print(stats.book_report(file_contents))
if __name__ == "__main__":
    main()