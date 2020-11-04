import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
forbidden = '":;,.-+=/\|[]{}()*^&"'
ok = 0
new_string = ""
for word in words:
    if word in forbidden:
        ok = 0
    else:
        new_string += word.lower()


words_split = new_string.split()

is_first = True
does_Exist = False
dictionary = {}
listy = []
for word in words_split:
    if is_first:
        is_first = False
        listy.append(word)
        dictionary[word] = []
    else:
        # listy.append(word)
        # check to see if the word already exists
        if dictionary.get(word, '00') != '00':
            dictionary[listy[0]].append(word)
            listy[0] = word
            does_Exist = True
        else:
            if does_Exist:
                does_Exist = False
                dictionary[listy[0]].append(word)
                dictionary[word] = []
                listy[0] = word
            
            else: 
                # if it doesn't exist create an entry in the dict
                dictionary[listy[0]] = [word]
                dictionary[word] = []
            
                # set the first index to current word
                listy[0] = word

# print(dictionary["that"])
# print(dictionary["this"])
# TODO: construct 5 random sentences
# for keys in dictionary.keys():
#     print(keys)

current = dictionary["it"]
new_sentence = ""
counting = 0
while current:
    counting += 1
    random_selection = random.choice(current)
    new_sentence += random_selection
    new_sentence += " "
    current = dictionary[random_selection]
    
    if counting > 30:
        break

print(new_sentence)
