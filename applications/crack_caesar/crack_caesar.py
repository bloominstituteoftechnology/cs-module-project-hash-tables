# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
alph = 'abcdefghijklmnopqrstuvwxyz'
alph = alph.upper()
# alph = alph.split(" , ")
print(alph)
file = open("ciphertext.txt","r")
# print(file.read( ))
# def caesar():
d = {}   

for i in range (len(alph)):
    d[alph[ i]] = i+4
      
    
print(d)   
print(hex(hash('hello')))         
    
