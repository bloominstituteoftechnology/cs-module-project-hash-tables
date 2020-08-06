# Your code here
def print_hist(l, max_length=10):
    text = ""
    for i in l:
        text += f"{i[0]:{max_length}s} " + "#" * i[1] + "\n"
    print(text)


def histo(s):
    d = {}
    m = 0
    ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ & ? !'.split(" ")
    for char in ignore:
        s = s.replace(char, "")
        s = s.lower()
    words = s.split()
    for word in words:
        if word not in d:
            d[word] = 0
            m = len(word) if len(word) > m else m
        d[word] += 1
    l = [x for x in d.items()]
    l.sort(key=lambda e: e[1], reverse=True)
    print_hist(l, m)


def file_word_count_histo(filename):
    with open(filename) as f:
        text = f.read()
    histo(text)


if __name__ == "__main__":
    file_word_count_histo("applications/histo/robin.txt")
