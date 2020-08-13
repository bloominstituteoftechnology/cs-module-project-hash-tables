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
def all_combos(numbers):
    numbers = list(numbers)
    plus = {}
    minus = {}
    f_answers = {}
    for num in numbers:
        answer = f(num)
        f_answers[num] = answer
    # index = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            plus_value = f(numbers[i]) + f(numbers[j])
            plus_key = (numbers[i], numbers[j])
            plus[plus_key] = plus_value

            minus_value = f(numbers[i]) - f(numbers[j])
            minus_key = (numbers[i], numbers[j])
            minus[minus_key] = minus_value
    # following variable error does not affect code #
    for (key1, value1) in plus.items():
        for (key2, value2) in minus.items():
            if plus[key1] is minus[key2]:
                print(f"f({key1[0]}) + f({key1[1]}) = f({key2[0]}) - f({key2[1]})  ***  {f_answers[key1[0]]} + {f_answers[key1[1]]} = {f_answers[key2[0]]} - {f_answers[key2[1]]}  ***  {plus[key1]} = {minus[key2]}")

all_combos(q) 





