# Your code here

ignore_list = '";:,.-+=/|\[]{}()*^&'

with open("robin.txt") as f:
    text = f.read().strip().split()
    # print(text)

cache = {}

for word in text:

    new_word = word.strip(ignore_list).lower()

    if new_word not in cache:
        cache[new_word] = 1

    else:
        cache[new_word] += 1

# print(cache)

# Sort the cache by the number of times each word occurs
# then reverse it to make the words that appear most first

sort_by_word_count = sorted(
    cache.items(), key=lambda item: item[1], reverse=True)
# print(sort_by_word_count)

greatest_number = len(sorted(cache.keys(), key=lambda x: len(x))[-1])
# print(greatest_number)

for k, v in sort_by_word_count:
    histo = ' ' * (greatest_number - len(k)) + v * '#'

    print(f"{k}  {histo}")
