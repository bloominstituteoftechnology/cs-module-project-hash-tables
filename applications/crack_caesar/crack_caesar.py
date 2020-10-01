# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# doing the imports of os to find the find dir
import os

thePath = r"C:\Users\porte\Richard_python\lambda\cs_lam\cs-module-project-hash-tables\applications\crack_caesar\ciphertext.txt"

the_file_obj =  open(thePath, "r")
theText = the_file_obj.read()
the_file_obj.close()



class mCeasars:
    def __init__(self):
        self.decode_table = {}
        self.word_frequency = {}
        self.most_frequent_used = [

            'E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
            'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z'
        ]
        

    # creating the function that will read in the file and then will decipther the code
    def decipheer(self, encoded_str):
        # need to to frequency analysis
        # need to do sorting of the hash table dictionary of the frequency analysis 
        # create the new key with the most frequent list
        # decode the text
        tupleList = self.frequency_anlysis(encoded_str)
        self.builNewDecoder(tupleList)
        return self.decode(encoded_str)



    def decode(self, encoded_str):
        """
        This function will decode the string and then will
        return the new decoded string
        """
        s = ""
        # looping through the chars in the text
        for l in encoded_str:
            if l.isalpha():
                l = l.lower()
            if l in self.decode_table:
                s += self.decode_table[l]
            else:
                s += l
        return s
    
    def frequency_anlysis(self, encoded_str, descending=True):
        """This function will do the frequency analysis and then do the sorting 
            By default will sort in largest values first and then descend from there.
            Will return a list of the keys and values in a tuple that are sorted in the way specified
        """
        for letter in encoded_str:
            # change to lower case if alpha
            if letter.isalpha():
                letter = letter.lower()
                if letter not in self.word_frequency:
                    self.word_frequency[letter] = 0
                self.word_frequency[letter] +=1 # incrrementing the count 

        # doing the sorting of the word frequency
        # making a list of the keys
        tupleList = [(k,v) for k ,v in self.word_frequency.items()]
        sortedList = sorted(tupleList, key= lambda e:e[1], reverse=descending)
        return sortedList

    def builNewDecoder(self, tupleList):
        """
        This function will make the new decoder that will be used to do the 
        decoding of the text
        It will be in the form of a dictionary with the key being the char and the val
        being the newChar decoded
        """
        # building the list
        for i in range(len(self.most_frequent_used)):
            if len(tupleList) <= i:
                # ran out of letters in the tuple
                break
            self.decode_table[tupleList[i][0]] = self.most_frequent_used[i]
        


if __name__ == "__main__":
    my = mCeasars()
    # theTuple = my.frequency_anlysis(theText)
    # print(theTuple)
    # my.builNewDecoder(theTuple)
    # print(my.decode_table)
    # print(len(my.decode_table))
    # print(my.decode(theText))
    print(my.decipheer(theText))

