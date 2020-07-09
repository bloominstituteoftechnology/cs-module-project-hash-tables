"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 50))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

# First Pass Solution

def all_combos(numbers):
    numbers = list(numbers)
    plus = {}
    minus = {}
    for num in numbers:
        answer = f(num)
        f_answers[num] = answer
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            plus_value = f(numbers[i]) + f(numbers[j])
            plus_key = (numbers[i], numbers[j])
            plus[plus_key] = plus_value
                
            minus_value = f(numbers[i]) - f(numbers[j])
            minus_key = (numbers[i], numbers[j])
            minus[minus_key] = minus_value
                
    for (key1, value1) in plus.items():
        for (key2, value2) in minus.items():
            if plus[key1] is minus[key2]:
                print(f"f({key1[0]}) + f({key1[1]}) = f({key2[0]}) - f({key2[1]})  ***  {f_answers[key1[0]]} + {f_answers[key1[1]]} = {f_answers[key2[0]]} - {f_answers[key2[1]]}  ***  {plus[key1]} = {minus[key2]}")

def all_solutions(numbers):
    numbers = list(numbers)
    plus = {}
    minus = {}
    minus_list = []
    count = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            plus_value = f(numbers[i]) + f(numbers[j])
            plus_key = (numbers[i], numbers[j])
            plus[plus_key] = plus_value
                
            minus_key = f(numbers[i]) - f(numbers[j])
            minus_value = (numbers[i], numbers[j])
            if minus_key not in minus:
                minus[minus_key] = [minus_value]
            else:
                minus[minus_key].append(minus_value)

    for (key, value) in plus.items():
            if value in minus:
                for item in minus[value]:
                    count += 1
                    print(f"f({key[0]}) + f({key[1]}) = f({item[0]}) - f({item[1]})  ***  {f(key[0])} + {f(key[1])} = {f(item[0])} - {f(item[1])}")
     
    print(f"Solution Count: {count}")

# all_combos(q)
import time
start_time = time.time()
all_solutions(q)
end_time = time.time()
print(f"Second Pass Solution took: {end_time - start_time}")
