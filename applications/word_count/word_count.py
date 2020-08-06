cache = {}

def word_count(s):
    # Your code here

    s = s.replace(".", "")
    s = s.replace(",", "")

    words = s.split(" ")
    print(words)
    for c in words:
        c
        if c not in cache:
            cache[c] = 0
        cache[c] += 1   


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))