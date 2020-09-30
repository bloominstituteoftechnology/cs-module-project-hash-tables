# Your code here
with open("robin.txt") as f:
	words = f.read().lower()

def replaceMultiples(mainString, toBeReplaced, newString):
	for elem in toBeReplaced :
		if elem in mainString :
			mainString = mainString.replace(elem, newString)
	return  mainString

cache = {}
all_words = words.split()
words_with_ignored = list(map(lambda st: replaceMultiples(st, ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&'], ""), all_words))
words_with_ignored.sort()
for word in words_with_ignored:
	if word not in cache:
		cache[word] = "#"
	else:
		cur_hash = cache[word]
		cur_hash = cur_hash+"#"
		cache[word] = cur_hash

sorted_cache = {k: v for k, v in sorted(cache.items(), key=lambda item: item[1], reverse=True)}
## Now we have our cache that is sorted by greatest used to least used.
print("\n".join("{0:<17}{1:<17}".format(k, v) for k, v in sorted_cache.items()))