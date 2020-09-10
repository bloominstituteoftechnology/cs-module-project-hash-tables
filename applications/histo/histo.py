# Your code here

esc = {char for char in ['\t', '\n', '\r']}

def word_count(s):
    # Your code here
    ht = {}
    word = ""
    special = {char for char in '":;,.-+=/\\|[]{}()*^& '}
    max_len = ""
    def add_word(word, max_len):
        if word not in ht:
            ht[word] = 1
        else:
            ht[word] += 1
        if len(word) > len(max_len):
            max_len = word
        return word if len(word) > len(max_len) else max_len
    for i in range(len(s)):
        if s[i] not in special:
            word += s[i].lower()
        if s[i] == ' ' and word:
            max_len = add_word(word, max_len)
            word = ''
    if word:
        max_len = add_word(word, max_len)
    return [ht, len(max_len)]

with open("robin.txt") as f:
    text = f.read()
    text = text.replace('\n', ' ').replace('\\', '')
    ht, max_len = word_count(text)
    
    ht = {k: v for k, v in sorted(ht.items(), key=lambda item: item[1], reverse=True)}
    
    sorted_list = []
    curr_list = []
    prev_count = 0
    for word in ht:
        if ht[word] != prev_count:
            curr_list.sort()
            sorted_list.append(curr_list)
            curr_list = []
            prev_count = ht[word]
        curr_list.append(word)
    
    for arr in sorted_list:
        for word in arr:
            bar = f"{word}{(max_len + 2 - len(word)) * ' '}{ht[word] * '#'}"
            print(bar)