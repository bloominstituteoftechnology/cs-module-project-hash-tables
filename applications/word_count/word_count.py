def word_count(s):
    s = s.translate(str.maketrans(s, s, ':,;.-+=/\|[]{}()*^&"'))
    s = s.replace("\n", " ")
    s = s.replace("\t", " ")
    s = s.replace("\r", " ")
    if len(s) == 0:
        return {}
        
    a = [w.lower() for w in s.split(" ") if w is not ""]
    
    d = {}
    for word in a:
        if word in d.keys():
            d[word]+=1
        else:
            d[word] = 1
    return d




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
