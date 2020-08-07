# cache = {}
# more than likely will need to be inside function 

def no_dups(s):
    cache = {}
    words_list = s.split()
    non_dups = [] 

    for words in words_list:

        if words not in cache:
            cache[words] = 1
            non_dups.append(words)

    new_sent = " ".join(non_dups)

    return new_sent


    # Your code here
    # first i will loop through the words with a regular loop
    # doing so will allow me to traverse through the words
    # i will want to use a cache to store each word i am itterating over
    # if the word is not in my cache i will add it to there
    # if the word is in my cache i will delete that word, 
    # i will find the delete at a certain index method
    # and i will mention i for the current position 
    # to delete that current word if it does exist in my cache

print(no_dups("the the the chungus is a mungus"))


# if __name__ == "__main__":
#     print(no_dups(""))
#     print(no_dups("hello"))
#     print(no_dups("hello hello"))
#     print(no_dups("cats dogs fish cats dogs"))
#     print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))