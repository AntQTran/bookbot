def get_num_words(file_contents: str) -> int:
    return len(file_contents.split())

def count_num_characters(file_contents: str) -> dict[str,int]:
    numAppeared: dict[str, int] = {}

    for c in file_contents:
        if c.lower() not in numAppeared:
            numAppeared[c.lower()] = 1
        else:
            numAppeared[c.lower()] += 1
    
    return numAppeared

def book_report(file_contents: str) -> str:
    num_words = get_num_words(file_contents)
    num_chars = count_num_characters(file_contents)

    output_str = """============ BOOKBOT ============\n
                Analyzing book found at books/frankenstein.txt...\n
                ----------- Word Count ----------\n"""
    output_str += f"Found {num_words} total words\n--------- Character Count -------\n"
    for k,v in dict(sorted(num_chars.items(), reverse=True, key=lambda x: x[1])):
        if k.isalpha():
            output_str += f"{k}: {v}\n"
    
    output_str += "============= END ===============\n"

    return output_str


