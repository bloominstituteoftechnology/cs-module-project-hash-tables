# Use frequency analysis to find the key to ciphertext.txt,
# and then decode it.

# Your code here
def letter_count(text):
    ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ & ? ! \''.split(" ")
    ignore.extend([" ", "\n"])
    counts = {}
    for i in text:
        if i not in counts and i not in ignore:
            counts[i] = 0
        if i not in ignore:
            counts[i] += 1
    return counts


def readfile(filename):
    with open(filename) as f:
        text = f.read()
    return text


def file_decode(filename):
    frequency_cipher = [
        "E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L", "W", "U", "G", "F", "B", "M", "Y", "C", "P", "K", "V", "Q", "J", "X", "Z"]
    text = readfile(filename)
    d = letter_count(text)
    l = [x for x in d.items()]
    l.sort(key=lambda e: e[1], reverse=True)
    l = [x for x in l if x[0].isalpha()]
    l.pop()
    l = [x for x, y in l]
    newText = ""
    for i in range(len(text)):
        if text[i].isalpha():
            try:
                index = l.index(text[i])
                newText += frequency_cipher[index]
            except:
                newText += text[i]
        else:
            newText += text[i]
    return newText


if __name__ == "__main__":
    print(file_decode("applications/crack_caesar/ciphertext.txt"))
