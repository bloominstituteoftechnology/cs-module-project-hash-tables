robin_text = open("robin.txt", "r")
remove_characters = ["\"", ":", ";", ",", ".", "-", "+", "=", "/", "\\",
			   "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", '', "!", "?"]
space = " "

word_tally = {}
word = ""

for character in robin_text.read().lower():
	if character in remove_characters:
		continue

	if character == space or character == "\n":
		if word in word_tally:
			word_tally[word] += 1
		else:
			word_tally[word] = 1
		word = ""
	else:
		word += character


# print(word_tally)
alphabetized_word_tally = sorted(word_tally.items(), reverse=True, key=lambda item: item[0])
sorted_word_tally = sorted(alphabetized_word_tally, key=lambda item: item[1])
sorted_word_tally = sorted_word_tally[::-1]


print(sorted_word_tally)
histogram = ""
number_of_spaces = 17

for item in sorted_word_tally:
	histogram += item[0]

	for i in range(0, number_of_spaces - len(histogram)):
		histogram += " "

	for i in range(0, item[1]):
		histogram += "#"
	print(histogram)
	histogram = ""