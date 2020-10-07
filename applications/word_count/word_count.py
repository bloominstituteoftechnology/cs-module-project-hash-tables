def word_count(s):
    # Replace unwanted chars
    for char in "\":;,.-+=/\|[]{}()*^&":
        s = s.replace(char, "")

    words = s.split()
    res = {}
    for word in words: 
        # Lower case just in case
        w = word.lower()
        if w in res: 
            # Word count plus 1 if word already exists
            res[w] += 1
        else: 
            # Add more if the new word not in dic
            res[w] = 1
    return res



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))