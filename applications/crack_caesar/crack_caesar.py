# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
key = {'A' : 'H',   'B' : 'Z',   'C' : 'Y',   'D' : 'W',   'E' : 'O',
    'F' : 'R',   'G' : 'J',   'H' : 'D',   'I' : 'P',   'J' : 'T',
    'K' : 'I',   'L' : 'G',   'M' : 'L',   'N' : 'C',   'O' : 'E',
    'P' : 'X',   'Q' : 'K',   'R' : 'U',   'S' : 'N',   'T' : 'F',
    'U' : 'A',   'V' : 'M',   'W' : 'B',   'X' : 'Q',   'Y' : 'V',
    'Z' : 'S'}
# Your code here

def cipher(message):
    message = list(message)
    print(message)
    for i in range(len(message)):
        if message[i] in key:
            message.insert(i, (key[message.pop(i)]))
            print(message[i], key[message[i]])
    message = "".join(message)
    print(message)
    return message

def decipher(message):
    message = list(message)
    reversekey = {}
    for i in key:
        reversekey[key[i]] = i
    print(message)
    for i in range(len(message)):
        if message[i] in reversekey:
            message.insert(i, (reversekey[message.pop(i)]))
            print(message[i], reversekey[message[i]])
    message = "".join(message)
    print(message)
    return message


with open("applications/crack_caesar/lorem.txt") as f:
    words = f.read()
    # words = cipher(''.join(words))
    print(words)
# with open("applications/crack_caesar/lorem.txt", 'w') as d:
#     d.write(words)

decipher('DOGGE, BEUGW!')
cipher('HELLO WORLD!')
