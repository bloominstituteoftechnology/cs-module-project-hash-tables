# Your code here
from collections import OrderedDict

with open("robin.txt") as f:
    words = f.read()
forbidden = ':;,.-+=/\|[]{}()*^&"'
new_string = ""
ok = 0
for word in words:
    if word in forbidden:
        ok = 0

    else:
        new_string += word.lower()

# print("- - - - ")
# print(new_string)

words_dict = {}
words_split = new_string.split()

if len(words) > 0:
    for word in words_split:
        if words_dict.get(word, '00') != '00':
            words_dict[word] += 1

        else:
            words_dict[word] = 1

# sorted_dict = sorted(words_dict.items(), key=lambda x:x[1])
# sorted_dict = sorted(words_dict, key=words_dict.get, reverse=True)
sorted_dict = sorted(words_dict.items(), key=lambda x:x[1], reverse=True)
# sortsy = OrderedDict(sorted(key, list(sorted(vals, reverse=True)))
#                             for key, vals in words_dict.items())
# print(sortsy)
increment = 0
for word in sorted_dict:
    string = '#'
    num_of_times = sorted_dict[increment][1]
    print(f"{word[0]} {string * num_of_times}")
    increment += 1




    

