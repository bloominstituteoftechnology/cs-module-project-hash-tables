from collections import Counter

def no_dups(s):
    # Your code here
    #split the string
    string = s.split(" ")
     
    for i in range(0, len(string)):
        #for string[i] - join string
        string[i] = "".join(string[i])
        #add to counter if duplicate exists
        dups = Counter(string)
        #strips the duplicate from the string and rejoins the string
        new_string = " ".join(dups.keys())
        return new_string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))