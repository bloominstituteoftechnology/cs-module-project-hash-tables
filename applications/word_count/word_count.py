def word_count(s):
    # Set a hash to keep track of words and their counts
    word_hash = {}

    # If empty string, return an empty hash
    if len(s) < 1:
        return {}
    
    remove_characters = ["\r", "\n", "\t"]

    for character in remove_characters:
        s = s.replace(character, " ")
    
    sArr = s.split(" ")
    for word in sArr:
        # Be able to ignore certain non-alphabetical characters
        stripped = ''.join([i for i in word if i not in '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'])
        
        if stripped.strip() == '':
            continue

        if stripped.lower() in word_hash:
            word_hash[stripped.lower()] += 1
        else:
            word_hash[stripped.lower()] = 1
    
    print('Hash', word_hash)
    return word_hash

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))