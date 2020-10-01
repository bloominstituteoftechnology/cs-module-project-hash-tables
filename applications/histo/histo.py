# Your code here

content = open('applications\histo\/robin.txt', 'r').read()

def word_count(s):
    # replace line breaks with spaces
    s = s.replace("\n", " ")
    # get rid of any char not (a-z) (a space) or (')
    reduced = ''
    s = [char.lower() for char in s if char.isalpha() or char == ' ' or char == '\'']
    for char in s: reduced += char
    # split the string into a list of words
    arr = reduced.split(' ')
    # create dict from words 
    wordCounter = dict.fromkeys(set(arr), ' ')
    # count words
    for word in arr: wordCounter[word] += '#'
    # Sort dict by value instead of key
    wordCounter = {k: v for k, v in sorted(wordCounter.items(), key=lambda item: item[1])}
    del wordCounter[''] 
    # return words
    for k in wordCounter:
        times = 15 - len(str(k))
        space = ' '
        print(f'{k}:{space * times}{wordCounter[k]}')


word_count(content)