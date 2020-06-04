def word_count(s):
    # Your code here
    words = s.lower()

    charr_whitespace = '\n \t \r'.split(" ") # coverting all whitespace characters to a space 
    
    for whitespace in charr_whitespace:
        words = words.replace(whitespace, " ")
    
    charr_to_forget = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ") #removing characters to be ignored
    
    for charr in charr_to_forget:
        words = words.replace(charr,"")
    
    words = words.split(" ") #turning string into an array of individual words
    
    words_you_are_looking_at = dict()
    
    for word in words:
        
        if word == "": # returns the control to the beginning of the loop
            continue # it rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.
        
        if word in words_you_are_looking_at:
            words_you_are_looking_at[word] += 1
        
        else:
            words_you_are_looking_at[word] = 1
    
    return words_you_are_looking_at







if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))