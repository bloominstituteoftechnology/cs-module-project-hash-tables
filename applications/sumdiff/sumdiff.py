"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
q = set(range(1, 200))
#q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

cache = {}

add_cache = {}
subtract_cache = {}

results = {}

# Log all values from f(x) in a cache
for i in q:
    if i not in cache:
        cache[i] = f(i)

cache_list = sorted(cache.items())

# Iterate through numbers in cache and log all a + b possibilities
for f in range(len(cache_list)):
    add_cache[(cache_list[f][0], cache_list[f][0])] = cache_list[f][1] + cache_list[f][1]

    for s in range(len(cache_list)):
        add_cache[(cache_list[f][0], cache_list[s][0])] = cache_list[f][1] + cache_list[s][1]

# Iterate through numbers in cache and log all c-d possibilities
    if f != s and s < len(cache_list):
        subtract_cache[(cache_list[s][0], cache_list[f][0])] = cache_list[s][1] - cache_list[f][1]

# Compare the add and subtract caches to find where the values are equal
for value in add_cache.items():
    if value[1] in subtract_cache.values():
        keys = list(subtract_cache.keys())[list(subtract_cache.values()).index(value[1])]

        for key in range(1, len(keys)):
            results[(value[0], value[1])] = ((keys[key - 1], keys[key]), subtract_cache[(keys[key - 1], keys[key])])

# Calculate results
results_list = sorted(results.items())

for result in results_list:
    a = result[0][0][0]
    b = result[0][0][1]
    c = result[1][0][0]
    d = result[1][0][1]

    a_result = cache[a]
    b_result = cache[b]
    c_result = cache[c]
    d_result = cache[d]

    print(f'f({a}) + f({b}) = f({c}) - f({d}) \t {a_result} + {b_result} = {c_result} - {d_result}')