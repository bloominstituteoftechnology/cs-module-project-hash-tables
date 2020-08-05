# Your code here
def histogram(filename):
    with open(filename) as f:
        words = f.read()
    word_list = words.replace("\n", " ").split()