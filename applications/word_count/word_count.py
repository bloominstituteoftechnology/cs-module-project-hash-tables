def word_count(s):

    words = s.split()
    dictionary = dict()

    for word in words:

    	word = word.lower().strip('":;,.-+=/\\|[]{}()*^&')

    	if word:
	    	if word not in dictionary:
	    		dictionary[word] = 1
	    	else:
	    		dictionary[word] += 1

    return dictionary 



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))