# Your code here
def histogram(filename):
    # get file's contents
    with open(filename) as f:
        s = f.read()
    
    # remove symbols, change to lowercase
    symlist = ['"',':',';',',','.','-','+','=','/','|','?',
              '\\','[',']','{','}','(',')','*','&','^','!']
    for symbol in symlist:
        s = s.replace(symbol, '')
    s = s.lower()

    wordlist = s.split()

    total_word_count = 0
    max_word_length = 0
    wordcounts = {}

    for word in wordlist:
        # get longest word
        if len(word) > max_word_length:
            max_word_length = len(word)

        # count words
        if word not in wordcounts:
            wordcounts[word] = 1
        else:
            wordcounts[word] += 1
        total_word_count += 1

    max_word_length += 2
    
    # sort by word counts
    wordcounts = sorted(wordcounts.items(), reverse=True, key=lambda item: item[1])

    # print results
    for word in wordcounts:
        printstr = ''
        printstr += word[0]
        printstr += ''.join([' ' for x in range(max_word_length-len(word[0]))])
        printstr += ''.join(['#' for x in range(word[1])])
        print(printstr)

if __name__ == "__main__":
    histogram('robin.txt')
