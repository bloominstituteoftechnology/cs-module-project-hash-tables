import random
import os

# Read in all the words in one go

def get_words():
    path = os.path.join(os.path.abspath(__file__), "..", "input.txt")
    with open(path) as f:
        words = f.read() # makes it just one long string
    return words


# making the dictonary that will contain the key "a word" and 
# the value as a list of the words that will follow that word.  The 
# list can have duplicates.
word_cache = {}
start_words = set()
stop_words = set()


# will split the string into a list
def split_to_list(theString):

    theList = theString.split()
    return theList

def isStop(theString):
    """
    Will return True if the word is a stop word
    """
    if theString.endswith((".", ".\"", "?", "?\"", "!", "!\"")):
        return True
    return False

# TODO: analyze which words can follow other words
# Your code here
def analyze(text):
    # need to go through the list of words will put in as the keys the word 
    # will then put in as value the words that follow it up and including the stop word
    # If the key is found further on in the text then more words will be added to it's list
    # until we hit another stop word
    for i in range(len(text)-1): # the minus one is to make it so that we can do the inner loop without going out of bounds
        if text[i] not in word_cache:
            # will add that word to the cache as a key
            word_cache[text[i]] = []
        # need to check if the word is a start Word to add to the set
        if((len(text[i]) > 1 and text[i][0] == "\"" and text[i][1].isupper()) or (text[i][0].isupper())): 
            start_words.add(text[i])
        
        # now need to begin from the point where the word is and move forward until we reach
        # a stop word
        # if the word is a stop word then there will be no words that follow it but
        # we will put the stop words in a dictionary also by themselves which then we can check to 
        # see if we have hit a stop word.  If we have we know to choose another random start word.
        for j in range(i+1, len(text)):
            
            # if in here will add the word to the list of the key
            word_cache[text[i]].append(text[j])
    
            if isStop(text[j]):
                # adding the stop word to a set
                stop_words.add(text[j])
                break # breaking from inner loop

def chooseStartWord():
    theChoice = ""
    if start_words:
        theChoice  =   random.choice(tuple(start_words))
        return theChoice
    return None


def chooseNextWord(word_key, sentance=""):
    theChoice = ""
    if word_key in word_cache:
        theChoice = random.choice(word_cache[word_key])
        if theChoice:
            # adding to the sentance 
            sentance += theChoice
            if theChoice in stop_words:
                return sentance
               
            else:
                sentance += " "
                return chooseNextWord(theChoice, sentance)
        
        
    return sentance     

      
                
def makeSentences(numSentancesMake):
    if numSentancesMake == None:
        raise Exception ("You need to enter the number of sentances to make")
    theStart = ""
    sentances = ""
    for i in range(numSentancesMake):
        while True:
            theStart = chooseStartWord()
            if theStart:
                break # breaking out of the while loop
        sentances += chooseNextWord(theStart, theStart+" ")
        sentances += " "
    return sentances



    

# TODO: construct 5 random sentences
# Your code here


if __name__ == "__main__":
    words = get_words()
    theList = split_to_list(words)
    analyze(theList)
    print("These are the start words")
    # print(start_words)
    # print("These are the stop words")
    # print(stop_words)
    # print("The word cache")
    # print(word_cache)
    print(makeSentences(5))

    
    
