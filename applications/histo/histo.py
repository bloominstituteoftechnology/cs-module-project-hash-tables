# Your code here

def histo(filename):
    ignored_list = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    dict_count = dict()
    total_count = 0
    max_length = 0
    


    with open("applications/markov/input.txt") as f:
        word_file = f.read() 


    for ch in ignored_list:
        word_file = word_file.replace(ch, '')
    word_file = word_file.lower()

    word_list = word_file.split()

    for word in word_list:     
        if len(word) > max_length:
            max_length = len(word)

        if word not in dict_count:
            dict_count[word] = 1
        else:
            dict_count[word] += 1        
        

    # sort using lambda
    # dict_count = sorted(dict_count.items(), key = lambda x: x[1], reverse = True)
    dict_count = sorted(dict_count.items(), key = lambda x: ( -x[1], x[0] ))
    # add to spaces
    max_length +=2

    for item in dict_count:
        print(f'{item[0].ljust(max_length)}' + '#' * item[1])

histo("applications/histo/robin.txt")        
