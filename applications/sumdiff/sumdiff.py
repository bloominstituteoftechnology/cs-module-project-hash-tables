"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

def f(x):
    return x * 4 + 6

cache = {}
sum_cache = {}
sub_cache = {}
result = {}

# Go through q and log all values from f(x) in a cache
for i in q:
    if i not in cache:
        cache[i] = f(i)

cache_list = sorted(cache.items())

# Go through items in cache and log all a + b possibilities in a sum cache
for f in range(len(cache_list)):
    sum_cache[(cache_list[f][0], cache_list[f][0])] = cache_list[f][1] + cache_list[f][1]

    for s in range(len(cache_list)):
        sum_cache[(cache_list[f][0], cache_list[s][0])] = cache_list[f][1] + cache_list[s][1]

        # Log all c - d possibilities in a sub cache
        if f != s and s < len(cache_list):
            sub_cache[(cache_list[s][0], cache_list[f][0])] = cache_list[s][1] - cache_list[f][1]

# Compare the sum and sub caches to find where the values are the same
for value in sum_cache.items():
    if value[1] in sub_cache.values():
        sub_keys = list(sub_cache.keys())[list(sub_cache.values()).index(value[1])]

        for key in range(1, len(sub_keys)):
            result[(value[0], value[1])] = ((sub_keys[key - 1], sub_keys[key]), sub_cache[(sub_keys[key - 1], sub_keys[key])])
        
# Print a formatted output with all potential combinations
result_list = sorted(result.items())

for result in result_list:
    a = result[0][0][0]
    b = result[0][0][1]
    c = result[1][0][0]
    d = result[1][0][1]

    a_result = cache[a]
    b_result = cache[b]
    c_result = cache[c]
    d_result = cache[d]

    print(f'f({a}) + f({b}) = f({c}) - f({d}) \t {a_result} + {b_result} = {c_result} - {d_result}')
