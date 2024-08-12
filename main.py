def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordCount = count_words(text)
    charCount = count_characters(text)
    print_report(book_path, wordCount, charCount)

def print_report(book_path, wordCount, charCount):
    header = f"--- Begin report of {book_path} ---"
    footer = ("--- End of report ---")
    print(header)
    print(f"{wordCount} words found in the document")
    print()
    for key in charCount.keys():
        print(f"The '{key}' character appears {charCount[key]} times")
    
    print(footer)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def count_characters(text):
    count_characters = {}
    for char in text:
      lower_char = char.lower()
      if not lower_char.isalpha():
          continue
      elif lower_char in count_characters:
          count_characters[lower_char] += 1
      else:
          count_characters[lower_char] = 1

    count_characters = dict(sorted(count_characters.items(), key=lambda item: item[1], reverse=True))
    return count_characters


if __name__ == "__main__":
    main()