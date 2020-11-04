def word_count(s):
    count_dict = {}
    words = ""
    punct_ignore = '":;,.-+=/\|[]{}()*^&'
    punct_count = 0

    for char in s:
        if char in punct_ignore:
            punct_count +=1

        if char not in punct_ignore:
            words = words + char
    
    if punct_count == 0:
        return count_dict
    
    else:
        words = words.split()
        words = [word.lower() for word in words]

        for word in words:
            if word in count_dict:
                count_dict[word] +=1
        
            else:
                count_dict[word] = 1
        
        return count_dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
