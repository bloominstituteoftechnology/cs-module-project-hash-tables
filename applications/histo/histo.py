# Your code here

with open ("applications/histo/robin.txt")as f:
    words = f.read()
    word_split  = words.split()
    
    
cache = {}   

for word in word_split:
    if word not in cache:
        cache[word] = '#'
    else:
        cache[word] += '#' 
        
items = list(cache.items()) 

items.sort(key = lambda x: x[1], reverse = True)     
print( "LEN",len(items))
for key, value in items:
    print(f'{key:<18} {value}') 