def word_count(string):
    separators = '":;,.-+=/\|[]{}()*^&'
    
    words = string.lower().split()
    counts = {}
    
    for word in words:
        word = word.strip(separators)
        if not word:
            break
        if word in counts:
            counts[word] += 1
        else: 
            counts[word] = 1
            
    return counts


# Driver program
if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
