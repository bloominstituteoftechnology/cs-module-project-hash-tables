# Your code here
import os

class Histo:
    def __init__(self, text_path=None, ignore="default"):
        # first will need to read in the text as ibe long string
        if text_path == None:
            text_path = os.path.join(os.path.realpath(__file__), "..",  "robin.txt")
        self.theText =self.__readFile(text_path)
        self.countFreq = {}
        if ignore == "default":
            self.ignore = {"\"" : "", ":":"" , ";":"", ",":"",  ".":"", "-":"", "\n":"",
                         "+":"",  "=":"",  "/":"", "\\":"", "|":"",  "[":"",  
                         "]":"",  "{":"",  "}":"",  "(":"",  ")":"",  "*":"",  "^":"",  "&":""}


    def __readFile(self, text_path):
        # read in the file and create a large string
        s = ""
        # path = os.path.join(os.path.realpath(__file__), "..", "robin.txt")
        with open(text_path, "r") as theFile:
            s = theFile.read()
        return s

    

    def make_histo(self):
        # Will need to run through the list and 
        # will run through the sorted dictio
        tupleList = self.split_string() # build the freqcount in the dictionary
        self.print_histo(tupleList)
    


    def print_histo(self, tupleList):
        print("\'\'\'\'")
        for i in range(len(tupleList)):
            print(tupleList[i][0].ljust(30, " "), end="")
            for j in range(tupleList[i][1]):
                print("#", end="")
            print()
        print("\'\'\'\'")



    def sort_word_freq(self, descending=True):
        """
        This is will sort the dictionary "wordFreq" default will be descending 
        "from largest to smallest"
        """
        # pull the key and val as a tuple and then make a list of them
        # sort the list and then put it back in the dictionary
        tupleList = [(k,v) for k, v in self.countFreq.items()]
        sortedTupleList = sorted(tupleList, key=lambda  e: e[1], reverse=descending)
        #self.countFreq = dict(tupleList) ---- not doing this right now
        return sortedTupleList


    def split_string(self,  descending= True):
        """
        This method will loop through the string and when the letter is a 
        space it will then put the string in the dictionary that will keep the count
        of the type of word
        """
        s = ""
        putInDict = 0
        for l in self.theText:
            if l not in self.ignore:
                # here we will add to the separated string
                if l == " ":
                    if putInDict == 1:  # in here we will put the string in the word count dictionary
                        if s not in self.countFreq:
                            self.countFreq[s] = 0
                        self.countFreq[s] +=1
                        putInDict = 0
                        s = ""
                else:
                    l = l.lower()
                    s += l
                    putInDict = 1
        return self.sort_word_freq(descending)
        

                    



if __name__ == "__main__":  
    my = Histo()
    my.make_histo()