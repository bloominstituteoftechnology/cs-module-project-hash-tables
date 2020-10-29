import re



def word_count(s):
    word_counts = {}
    ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    words = s.split()

    print(f'Word list : {words}')
    
    for word in words:
        new_word = ""
        for letter in word:
            if letter not in ignore:  
                new_word += letter

        next_word = new_word.lower()

        if next_word in word_counts:
            word_counts[next_word] += 1
        elif next_word == "" or next_word == " ":
            return {}
        else:
            word_counts[next_word] = 1

    if s == "":
        return {}
    else:
        return word_counts

if __name__ == "__main__":
    # print(word_count(""))
    # print(word_count("Hello"))
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

    print(word_count('This is a test of the  Emergency  Broadcast  Network. This is only a test.'))
    #{'this': 2, 'is': 2, 'a': 2, 'test': 2, 'of': 1, 'the': 1, 'emergency': 1, 'broadcast': 1, 'network': 1, 'only': 1})
    #{'this': 1, 'is': 2, 'a': 2, 'test': 2, 'of': 1, 'the': 1, 'emergency': 1, 'broadcast': 1, 'network': 1, 'only': 1}