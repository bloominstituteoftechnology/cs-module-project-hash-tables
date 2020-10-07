# Your code here
def histogram(file):
    # Read in all the words in one go
    with open(file) as f:
        words = f.read()

    # Set a hash to keep track of words and their counts
    word_hash = {}
    words = words.replace('\n', " ")
    wordArr = words.split(" ")
    longest_word = wordArr[0]

    for word in wordArr:
        # Be able to ignore certain non-alphabetical characters
        stripped = ''.join([i for i in word if i not in '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'])
        
        if stripped.strip() == '':
            continue

        if stripped.lower() in word_hash:
            word_hash[stripped.lower()].append('#')
        else:
            word_hash[stripped.lower()] = ['#']
            if len(word) > len(longest_word):
              longest_word = word
    
    high_to_low = sorted(word_hash.items(), key = lambda x: x[1], reverse = True)

    for i in high_to_low:
      word = i[0]
      hash_count = ''.join(i[1])
      spaces = (len(longest_word) + 2) - len(word)
      print(word + spaces*" " + hash_count)

histogram('robin.txt')
