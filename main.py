def count_words(text):
	text_array = text.split()
	return len(text_array)

def main():
	with open('books/frankenstein.txt') as f:
		file_contents = f.read()
		print(count_words(file_contents))



main()