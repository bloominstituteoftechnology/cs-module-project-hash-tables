def word_count(s):
    #input is a string
    #output should be dictionary with key strings; values should be counted
    #output should be lowercase
    #cases ignored: (" : ; , . - + = / \ | [ ] { } ( ) * ^ &)
    #if input is empty or contains ignored cases return empty dictionary
    # Your code here

   words = {}
   ignored =  '":;,.-+=/\\|[]{}()*^&'

   for ignors in ignored:
       if s == "" or s == ignored:
           return words

   for word in s.split():
       if not word.lower()[-1].isalnum() and not word.lower()[0].isalnum():
            if word[1:-1] in words:
                words[word[1:-1]] += 1
            else:
                words[word[1:-1]] = 1
       elif not word.lower()[-1].isalnum():
           if word.lower()[:-1] in words:
               words[word.lower()[:-1]] += 1
           else:
               words[word.lower()[:-1]] = 1
       else:
           if word.lower() in words:
               words[word.lower()] += 1
           else:
               words[word.lower()] = 1


   return words













if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))







