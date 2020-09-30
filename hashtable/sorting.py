d = {
  'foo' :12,
  'bar': 10,
  'qux':21
    
}

mylist = list(d.items())
mylist.sort(reverse= True)
# print(sorted(d.items()))
# for i in mylist:
#     print(i)
    
mylist.sort(reverse = True ,key = lambda tupl:tupl[1])   
for i in mylist:
    print(i)
    
    
##HERE YA GO CODEWARS print num of occurences of each letter

string_to_count = "The quick brown fox jumps over the lazy dog"   

def letter_counts(s):
    d = {}
    
    for letter in s:
        if letter == "":
           continue
        if letter not in d:
            d[letter]=1
        else:
            d[letter] +=1
        return d    
            
def print_letters(s) :
    counts_dict = letter_counts(s)
    letter_counts(string_to_count)  
    counts_list = list(counts_dict.items())
    counts_list.sort(reverse = True, key = lambda x: x[1])    
    
    for pair in counts_list:
        print(f'count: {pair[1]} letter: {pair[0]}')      


print_letters(string_to_count)