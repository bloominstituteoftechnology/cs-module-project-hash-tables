from collections import Counter

with open("./robin.txt", "r") as f:
    content = f.read()

s = content.translate(str.maketrans(content, content, ':,;.-+=/\|[]{}()*^&"'))
s = s.replace("\n", " ")
s = s.replace("\t", " ")
s = s.replace("\r", " ")
if len(s) == 0:
    print("error")

a = [w.lower() for w in s.split(" ") if w is not ""]

c = Counter(a)
indent = len(max(a, key=len)) + 2
l = sorted(c, key=lambda k: (-c[k], k))

for w in l:
    s = (indent - len(w)) * " "
    h = c[w] * "#"
    print(f"{w}{s}{h}")

