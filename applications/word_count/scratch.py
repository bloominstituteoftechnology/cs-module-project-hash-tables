string = "Testing"
lowercase = string.lower()
for word in lowercase.split():
    print(word)

ignore_chars = '" : ; , . : - + = / \ | [ ] { } ( ) * ^ &'.split(" ")



cache={}
for chars in ignore_chars:
    if chars not in cache:
         cache[chars] = 1
    else:
        cache[chars] +=1
   


print(cache)


def no_dups(string):
    for words in string.split():
        
        
    return cache[words]
        
print(no_dups("hello hello"))

