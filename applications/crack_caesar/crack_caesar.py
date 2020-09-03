# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

with open("ciphertext.txt") as f:
    message = f.read()

punc = ":;,.-+= /\\|[]{}()*^&\""

s = message
for ele in s:
    if ele in punc:
        s = s.replace(ele, "")

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

frequency = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
             'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
# builds empty count_list ([0,0,0...0,0])
count_list = []
i = 0
while i < 26:
    count_list.append(0)
    i += 1
    # converts message string to array
    array = []
for i in s:
    array.append(i)
n = len(array) + 0.0
# counts occurences of each letter
for x in array:
    i = 0
    while i < 26:
        if x == alphabet[i]:
            count_list[i] += 1
        i += 1
# normalizes frequencies
freq_list = []
for x in count_list:
    freq_list.append(x/n * 100)

original_dict = dict(zip(alphabet, freq_list))
decoder_dict = dict(zip(sorted(freq_list, reverse=True), frequency))

translator = {}
for k, v in original_dict.items():
    translator[k] = decoder_dict[v]

for k, v in translator.items():
    print(k, v)

results = ''
for ele in message:
    if ele in alphabet:
        results += translator[ele]
    else:
        results += ele

print(results)
