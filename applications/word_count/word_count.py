def word_count(s):
    # These are the cases we have to ignore
    ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    # Split so we can split the repeated runs of whitespace
    words = s.split()
    counts = {}

    # We'll loop through our words
    for word in words:
         new_word = ""
         for char in word:
             # if the characters are not in our ignore cases
             if char not in ignore:
                 # Then we can use string concatenation to add it to our new_word variable
                 new_word += char
        # This will lowercase our word
         word = new_word.lower()

         if word in counts:
             counts[word] += 1
         elif word == "" or word == " ":
             break
         else:
             counts[word] = 1

    # If the input is empty, we return an empty dict
    if s == "":
        return {}
    else:
        return counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
