import re
def word_count(s):
    # Your code here
    if s == '':
        return {}
    count_dict = {}
    str_list = s.split()
    # str_list = re.split('|\t|\n|\r', s)
    for word in str_list:
        single_word = word.lower()
        # This below like remove the special characters from the word.
        special_characters = r"""!"#$%&"()*+,-./:;<=>?@[\]^_`{|}~"""
        trimmed_word = ''.join(character for character in single_word if character not in special_characters)
        if trimmed_word not in count_dict:
            if len(trimmed_word) >= 1:
                count_dict[trimmed_word] = 1
        else:
            count_dict[trimmed_word] += 1    
    print(count_dict)
    return count_dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))