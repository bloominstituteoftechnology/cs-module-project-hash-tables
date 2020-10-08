# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here


# plaintext
plain_txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ciphertext
cipher_txt = open("applications/crack_caesar/ciphertext.txt", "r")
# print(cipher_txt.read())


from collections import Counter 

encryption = cipher_txt.read(25)
# print(encryption)  
# initializing string  
test_str = encryption
  
# using collections.Counter() to get  
# count of each element in string  
res = Counter(test_str) 
  
# printing result  
print ("key/value --> encryption  :\n " +  str(res)) 



shift = 3 # defining the shift count




for c in plain_txt:

    # if character is  uppercase letter
    if c.isupper():

        # find the position in 0-25 , Return the Unicode code point for a one-character string.
        c_unicode = ord(c)

        c_index = ord(c) - ord("A")

        # use the shift=3 + c_index  modulo by 26
        new_index = (c_index + shift) % 26

        # convert to new character
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # append to encrypted string
        encryption = encryption + new_character

    else:

        # not uppercase
        encryption += c
        
print("Encrypted text:",encryption)
# print("Plain text:",plain_txt)




