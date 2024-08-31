def sort_on(dict):
	return dict["count"]

def dict_to_dictlist(dict):
	dict_list = []
	for key in dict:

		if not key.isalpha():
			continue

		char = key
		count = dict[key]

		new_dict = {"char": key, "count": count}
		dict_list.append(new_dict)
	
	return dict_list


def count_characters(text):
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
		
		word_count = count_words(file_contents)
		characters = dict_to_dictlist(count_characters(file_contents))
		characters.sort(reverse=True, key=sort_on)

		print("--- Begin report of books/frankenstein.txt ---")
		
		print(f"> {word_count} words found in the document\n")
		
		for char in characters:
			print(f"The '{char["char"]} character was found {char["count"]} times")
			pass

		print("--- End Report ---")


main()