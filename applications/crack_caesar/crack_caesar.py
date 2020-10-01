# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open("ciphertext.txt") as f:
    text = f.read()
    text = text.replace('\n', ' ').replace('\\', '')
    ht = {}
    count = 0
    for char in text:
        if ord(char) >= 65 and ord(char) <= 90:
            if char not in ht:
                ht[char] = 1
            else:
                ht[char] += 1
            count += 1 
    frequent_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']    
    ht = { k[0]: frequent_list[i]  for i, k in enumerate(sorted(ht.items(), key=lambda item: item[1], reverse=True))}
    for char in text:
        if ord(char) >= 65 and ord(char) <= 90:
            print(ht[char], end="")
        else:
            print(char, end="")