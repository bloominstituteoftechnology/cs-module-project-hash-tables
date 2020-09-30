def word_count(s):
    #input is a string
    #output should be dictionary with key strings; values should be counted
    #output should be lowercase
    #cases ignored: (" : ; , . - + = / \ | [ ] { } ( ) * ^ &)
    #if input is empty or contains ignored cases return empty dictionary
    # Your code here

   words = {}
   ignored = ' " : ; , . - + = / \ | [ ] { } ( ) * ^ & '

   for ignors in ignored:
       if s == "" or s == str(ignors):
           return words

   for word in s.split():
       if word.lower() not in words:
           words[str(word.lower())] = 1

       elif word.lower() in words:
           words[str(word.lower())] += 1


   print(words)











# if __name__ == "__main__":
# #     print(word_count(""))
# #     print(word_count("Hello"))
# #     print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
# #     print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

word_count('Hello Hello')