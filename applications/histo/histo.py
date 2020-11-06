# Your code here
histo = {}
longest = 0
ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', '?', '!']

theFile = open("robin.txt", "r")

for line in theFile.readlines():
    clean_line = "".join(ch for ch in line if ch not in ignore).lower()
    for word in clean_line.split():
        if word not in histo:
            histo[word] = "#"
            if len(word) > longest:
                longest = len(word)
        else:
            histo[word] = histo[word] + "#"

sorted_histo = sorted(histo.items(), key=lambda x: x[0], reverse=False)
# sorted_histo_o = sorted(sorted_.items(), key=lambda x: x[0], reverse=False)


# for word in histo:
#     just = longest + 2
#     print(f"{word.ljust(just)} {histo[word]}")

print(sorted_histo)
# print(histo)


# def word_count(s):
#     frequency = {}
#     ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    
#     clean_string = "".join(ch for ch in s if ch not in ignore)
#     for word in clean_string.lower().split():
#         if word not in frequency:
#             frequency[word] = 1
#         else:
#             frequency[word] += 1
            
#     return frequency

theFile.close()

