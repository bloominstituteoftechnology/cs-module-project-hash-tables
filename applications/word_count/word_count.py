from functools import reduce 

# global vars
ignore_str = '":;,.-+=/\\|[]{}()*^&'

def word_count(words: str) -> dict:
    no_punct_words = words.translate(
        str.maketrans('','',ignore_str)).lower().split()
    # return dict((word, no_punct_words.count(word)) for word in no_punct_words)
    return (reduce( lambda return_dict, 
        count: return_dict.update([(count, return_dict.get(count,0)+1)]) 
        or return_dict, no_punct_words, {}) )



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))