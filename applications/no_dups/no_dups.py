def no_dups(s):
    # Your code here


     key_str = ""
 
     words = s.split()
     dict_keys = dict() 
     for item in words:
          if item not in dict_keys.keys():
               dict_keys[item] = item 
               key_str += item + ' '

     # num_keys = len(dict_keys)
     # print(f' length of dict_keys {num_keys}')
     # for k,v in dict_keys.items():
     #      if num_keys > 1:
     #           key_str += k + ' '
     #      else:
     #           key_str += k     
     #      num_keys -= 1
     
     return key_str.strip()  # removes beg & end spaces in string
     # print(f' {key_str}')


if __name__ == "__main__":
     print(no_dups(""))
     print(no_dups("hello"))
#     print(no_dups("hello hello"))
#     print(no_dups("cats dogs fish cats dogs"))#
#    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))