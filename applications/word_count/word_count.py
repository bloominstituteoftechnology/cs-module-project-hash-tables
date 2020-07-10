
ignored = ['"', ':', ';', ',', '.', '-', '+', '=', '\\','/', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
def word_count(s):
    # Your code here
    cache = {}
    
    wordList = s.split()

    for word in wordList:
        word = word.lower()
        for badChar in ignored:
            word = word.replace(badChar, "")

        if word in cache:
            cache[word] += 1
        elif word =="" or word ==" ":
            break
        else:
            cache[word] = 1
    return cache
if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\|[]{}()*^&'))