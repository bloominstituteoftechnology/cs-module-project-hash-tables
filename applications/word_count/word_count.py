def word_count(s):
     # Your code here

     
     ignored_list = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
     
     # remove any ch in ignored_list and make s all lowercase
     for ch in ignored_list:
          s = s.replace(ch, "").lower()
     
     count_dict = dict()
     word_list = s.split()

     for word in word_list:
          if word not in count_dict:
               count_dict[word] = 1
          else:
               count_dict[word] += 1     

     return count_dict

if __name__ == "__main__":
     print(word_count(""))
     print(word_count("Hello"))
     print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
     print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

