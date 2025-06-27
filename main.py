#!/usr/bin/env python3

import stats
def get_book_text(file_path: str, ) -> str:
    with open(file_path, 'r') as f:
        file_contents = f.read()
        return file_contents



def main():
    file_contents = get_book_text("books/frankenstein.txt")
    print(f"{stats.get_num_words(file_contents)} words found in the document")

    print(stats.count_num_characters(file_contents))

    print(stats.book_report(file_contents))
if __name__ == "__main__":
    main()