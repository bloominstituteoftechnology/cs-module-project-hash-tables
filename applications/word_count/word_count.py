

def word_count(string):
    edge_cases = [":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\""]
    dictionary = dict()
    lower_case_string = string.lower()

    for item in edge_cases:
        lower_case_string = lower_case_string.replace(item, "")

    lower_case_string = lower_case_string.split()

    for item in lower_case_string:
        if item in dictionary:
            x = dictionary[item]
            x += 1

            dictionary[item] = x
        else:
            dictionary[item] = 1

    return dictionary



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))