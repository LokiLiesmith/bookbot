def count_words(text):
	num_words = len(text.split())
	return num_words

def count_characters(text):
	lower_case = text.lower()
	result = {}
	for i in sorted(set(lower_case)):
		result[i] = lower_case.count(i)
	return result

def sort_on(items):
	# print(f"{items["num"]}")
	return items["num"]

def expand_dict(dict):
	list = []
	for i in dict:
		smol = {"char" : i, "num" : dict[i]}
		list.append(smol)
	list.sort(reverse=True, key=sort_on)
	return (list)
