# grabbing alphabet from this
import string

# Import encrypted message
content = open('applications\crack_caesar\ciphertext.txt', 'r').read()
# Import decoder
decoder = ['z','x','j','q','v','k','p','c','y','m','b','f','g','u','w','l','d','s','i','r','n','h','o','a','t','e']
# Remove non alphabetical characters from encrypted message and convert them all to lowercase.
reducedContent = [char.lower() for char in content if char.isalpha() and char != 'â'] # <- Last part is super annoying. It was turning '-' into this char
# Create dict of english alphabet -> ( Key = character, value = count )x26
charCounter = dict.fromkeys(string.ascii_lowercase, 0) # ( a, 0 )..( b, 0 )..( c, 0 )... ect... e
# Use dict to count letters
for char in reducedContent: charCounter[char] += 1
# Convert count into percentage.  count / total chars
for letter, count in charCounter.items():
    charCounter[letter] = count / len(reducedContent)
# Sort dict by value instead of key
charCounter = {k: v for k, v in sorted(charCounter.items(), key=lambda item: item[1])}
# Replace numeric dict values with decoder values
for count, (key, value) in enumerate(charCounter.items()):
    charCounter[key] = decoder[count]
# create empty output string
output = ''
# loop over every char in encrypted message
for char in content:
    # exact char is in dict? -> ok swap that char with dict value
    if char in charCounter:
        output += charCounter[char]
    # lowercase version of char is in dict? -> ok swap that char with dict value
    elif char.lower() in charCounter:
        output += charCounter[char.lower()].upper()
    # if it's not in the dict just leave it as is.
    else: output += char
#print output
print(output)

