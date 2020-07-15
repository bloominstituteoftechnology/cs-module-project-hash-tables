import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
cache = {}
all_words = words.split()
for i in range(len(all_words)):
	if i == 0:
		## We don't have a previous word, so lets set it
		prev_word = all_words[i]
	else:
		if prev_word not in cache:
			## This word doesn't exist in cache, so lets add it with the word that follows
			cache[prev_word] = [all_words[i]]
		else:
			## Here we are getting our list of follow words from cache, then appending this word
			cur_list = cache[prev_word]
			cur_list.append(all_words[i])
			cache[prev_word] = cur_list
		prev_word = all_words[i]
## Cache now holds all of our words whith which words can follow
punc = ['.', '?', '!']
start_words = []
end_words = []
keys = cache.keys()
for key in keys:
	if (key[0].isupper() or key[0] == '"' and key[1].isupper()) and (key[-1] != '"') and (key[-1] not in punc):
		start_words.append(key)
	if (key[-1] in punc) or (key[-1] == '"' and key[-2] in punc):
		end_words.append(key)
## We now have our start_words and our end_words

# TODO: construct 5 random sentences
# Your code here
new = True
sentence = 0
while sentence < 5:
	if new:
		word = random.choice(start_words)
		print(word, end=" ")
		new = False
	else:
		if word in end_words:
			new = True
			sentence += 1
		else:
			cur_list = cache[word]
			word = random.choice(cur_list)
			print(word, end=" ")
