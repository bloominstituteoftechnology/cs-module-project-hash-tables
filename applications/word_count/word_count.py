def word_count(s):
    # Your code here
    inputString = s.split(" ")
    ignore = ['"', ":", ";", ",",".","-","+","=","/","\\","\r","\n","\t","|","[","]","{","}","(",")","*","^","&"]
    counts = {}
    for word in inputString:
        letters = []
        for char in word:
            if char in ignore:
                newChar = "_"
            else:
                newChar = char

            letters.append(newChar)
        
        newWord = ''.join([char.lower() for char in letters])
        if "_" in newWord:
            newWordsArray = newWord.split("_")
            for word in newWordsArray:
                if word != "" and word != " ":
                    if word in counts:
                        counts[word] += 1
                    else:
                        counts[word] = 1
        else:
            if newWord != "":
                if newWord in counts:
                    counts[newWord] += 1
                else:
                    counts[newWord] = 1
    return counts




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))