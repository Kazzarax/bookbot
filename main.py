import sys
from stats import get_characters
from stats import get_num_words
from stats import sorter


def get_book_text(filePath):
	with open(filePath) as f:
		file_content = f.read()
		return file_content

def generate_report(bookFile):
	numWords = get_num_words(get_book_text(bookFile))
	print(f"============ BOOKBOT ============\nAnalyzing book found at {bookFile}...")
	print("----------- Word Count ----------")
	print(f"Found {numWords} total words")
	print("--------- Character Count -------")
	for k, v in sorter(get_characters(get_book_text(bookFile))).items():
		print(str(k) + ": " + str(v))
	print("============= END ===============")

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		bookFile = sys.argv[1]
		generate_report(bookFile)

if __name__ == "__main__":
	main()
