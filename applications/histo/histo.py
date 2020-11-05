# Your code here

ignore_str = '":;,.-+=/\\|[]{}()*^&'
pad = 2

with open('robin.txt') as f:
	# set as a string 
	my_list = f.read().replace('\n', '')

# helper function copy pasted from word_count because relative imports are terrible 
def word_count(words: str) -> dict:
    no_punct_words = words.translate(
        str.maketrans('','',ignore_str)).lower().split()
    # print(no_punct_words)
    return dict((word, no_punct_words.count(word)) for word in no_punct_words)

# helper function to print hashes in loop
def print_hashes(int):
	return(int * "#")

# print histogram of word counts to console 
def print_histograms(words_dict: dict) -> None:
	longest_key = max(len(x) for x in wc_dict) + 2
	# have to sort keys alphabetically which is done with key =, and values by descending which is done with sorted()
	# read more here: 
	# https://stackoverflow.com/questions/9919342/sorting-a-dictionary-by-value-then-key
	sorted_tuple = sorted(wc_dict.items(), key = lambda wc_dict: (-wc_dict[1],wc_dict[0]), reverse=False)
	for k, v in sorted_tuple:
	#	print("{0:<17}".format(k), v * "#")
		print(f"{k:<{longest_key}} {print_hashes(v)}")

wc_dict = word_count(my_list)
print_histograms(wc_dict)