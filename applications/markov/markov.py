import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
d = {}
newwords = words.replace("\n", " ")
newnewwords = newwords.split(" ")
def analyze(w):
    
    for i, j in enumerate(w):
        if(i+1 == len(w)):
            return d
        if(j not in d):
            d[j] = []
        if(w[i+1] not in d[j]):
            d[j].append(w[i+1])

analyze(newnewwords)
# TODO: construct 5 random sentences
# Your code here
startlist = d[random.choice(newnewwords)]
startword = random.choice(startlist)

def construct_sent(starter):
    sentences = ""
    
    for i in range(len(words)):
        if("." in starter or "!" in starter or "?" in starter):
            return starter
        else:
            if(len(starter) == 0):
                starter = random.choice(d[random.choice(newnewwords)])                
            elif(starter[0].isupper() == True or (starter[0] == '"')):
                break
            else:
                print(starter, end=" ")
                starter = random.choice(d[random.choice(newnewwords)])
    randoword = random.choice(d[starter])

    
    count = 0
    worded = starter         
    while("." not in starter or "!" not in starter or "?" not in starter):
        newchoice = random.choice(d[worded])
        starter += newchoice + " "
        worded = newchoice
    return starter

print(construct_sent(startword))