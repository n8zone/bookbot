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
	char_count_dict = {}
	for c in text:
		print(f"c: {c}")
		if c not in char_count_dict:
			char_count_dict[c] = 0
		char_count_dict[c] += 1

	return char_count_dict


def count_words(text):
	text_array = text.split()
	return len(text_array)

def filter_by_character(chars, text):
	text_copy = text
	lowered_text = text_copy.lower()
	split_text = lowered_text.split()
	words_containing_pattern = list(filter(lambda word: chars in word, split_text))
	return words_containing_pattern, len(words_containing_pattern)

def main():
	with open('books/frankenstein.txt') as f:
		file_contents = f.read()
		
		word_count = count_words(file_contents)
		search_term = input("What substring would you like to search for?\n")
		words_with_term, count_with_term = filter_by_character(search_term, file_contents)
		
		characters = dict_to_dictlist(count_characters(file_contents))
		characters.sort(reverse=True, key=sort_on)

		print("--- Begin report of books/frankenstein.txt ---")
		
		print(f"> {word_count} words found in the document\n")
		
		for char in characters:
			print(f"The '{char["char"]}' character was found {char["count"]} times")
			pass
		print(f"\nThe substring: {search_term} was found {count_with_term} times!")
		print(f"Words containing: {words_with_term}")

		print("--- End Report ---")


main()