
def word_count(s):
    cache = {}
    for word in s.split():
        word = word.lower()

        punctuation = '":;,.-+=/\\|[]{}()*^&'
        for character in word:
            if character in punctuation:
                word = word.replace(character, "")
        
        if word in cache:
            cache[word] += 1
        elif word != '':
            cache.update({ word: 1 })

    print(f'Cache: {cache}')
    return cache



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))