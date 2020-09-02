




def word_count(s):
    if s == '': return
    # get rid of any char not (a-z) (a space) or (')
    reduced = ''
    s = [char.lower() for char in s if char.isalpha() or char == ' ' or char == '\'']
    for char in s: reduced += char
    # split the string into a list of words
    arr = reduced.split(' ')
    # create dict from words 
    wordCounter = dict.fromkeys(set(arr), 0)
    # count words
    for word in arr: wordCounter[word] += 1
    # return words
    return str(wordCounter)


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))