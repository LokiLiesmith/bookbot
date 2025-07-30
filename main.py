import sys
from stats import count_words, count_characters, expand_dict

def	main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
	book_path = sys.argv[1]
	text = get_book_text(book_path)
	num_words = count_words(text)
	num_chars = count_characters(text)
	sorted_list = expand_dict(num_chars)
	# print(f"{num_words} words found in the document")
	# print(f"{num_chars}")
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for i in sorted_list:
		if i["char"].isalpha():
			print(f"{i["char"]}: {i["num"]}")
	print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()