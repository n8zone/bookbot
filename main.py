def count_character(text):
	text = text.lower()
	text_array = text.split()
	char_count_dict = {}
	for w in text_array:
		for c in w:
			if c not in char_count_dict:
				char_count_dict[c] = 0
			char_count_dict[c] += 1

	return char_count_dict


def count_words(text):
	text_array = text.split()
	return len(text_array)

def main():
	with open('books/frankenstein.txt') as f:
		file_contents = f.read()
		print(count_words(file_contents))

		print(count_character(file_contents))



main()