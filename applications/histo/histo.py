# Your code here
import codecs
print(codecs.encode(
    "Items: .vgrzf() zrgubq ba n qvpgvbanel zvtug or hfrshy. vg'f cbffvoyr sbe .fbeg() gb fbeg ba zhygvcyr xrlf ng bapr. artngvirf zvtug uryc jurer erirefr jba'g. lbh pna cevag n inevnoyr svryq jvqgu va na s-fgevat jvgu arfgrq oenprf, yvxr fb", "rot13"))

# start here
with open("robin.txt") as f:
    words = f.read()

# words = "Round the rugged rock the freak freak freak insanity! Don't forget to ruN to the stoRE, you freak!"


def word_count(s):
    new_list = s.lower().split()
    # forbidden characters
    forbidden = '":;,.-+=/\|[]}{()?!*^&'
    storage = {}
    for word in new_list:
        word = word.lower()
        for letter in word:
            if letter in forbidden:
                word = word.replace(letter, "")
        if word == "":
            return {}
        if word in storage:
            storage[word] = storage[word] + "#"
        if word not in storage:
            storage[word] = "#"

    for key, value in sorted(storage.items(), key=lambda x: -len(x[1])):
        print(f'{key: <16}{value}')


word_count(words)
