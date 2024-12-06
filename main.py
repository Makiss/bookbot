def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        chars_count = count_chars(file_contents)
        print_report(word_count, chars_count)

def count_words(string):
    return len(string.split())

def count_chars(string):
    chars_count = {}

    for char in string.lower():
        if char.isalpha():
            if not char in chars_count:
                chars_count[char] = 0
            chars_count[char] += 1
    return chars_count

def print_report(word_count, chars_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("\n")
    for char in chars_count:
        print(f"The '{char}' character was found {chars_count[char]} times")
    print("--- End report ---")

main()
