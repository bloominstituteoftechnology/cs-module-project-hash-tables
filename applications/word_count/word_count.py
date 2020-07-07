import re
def word_count(s):
    # Your code here
    words = re.sub(r'[":;,.\-+=/\\|\[\]{}()*^&]', ' ', s)
    count = {}
    for word in words.split():
        count[word.lower()] = 1 if word.lower() not in count else count[word.lower()] + 1
    return count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))