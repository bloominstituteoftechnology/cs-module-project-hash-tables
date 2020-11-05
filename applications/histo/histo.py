# Your code here

ignore = '"":;,.-+=/\\|[]{}()*^&'
counts = {}
longest = ""

with open("robin.txt", encoding="utf8") as f:
    words = f.read().strip().replace("\n", " ").split(" ")


def count_occurrences(words):
    for word in words:
        word = word.strip(ignore).lower()

        if word not in counts and word != "":
            counts[word] = 1
        elif word != "":
            counts[word] += 1


def find_longest_word(words):
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def sort_list():
    sorted_list = list(counts.items())
    sorted_list.sort(key=lambda x: (x[1], x[0]), reverse=True)

    return sorted_list


def print_historgram(sorted_list, longest_word_len):
    for item in sorted_list:
        hist = " " * (longest_word_len - len(item[0])) + "#" * item[1]
        print(f"{item[0]} {hist}")


def run(words):
    count_occurrences(words)
    longest = find_longest_word(words)
    print_historgram(sort_list(), len(longest))


run(words)