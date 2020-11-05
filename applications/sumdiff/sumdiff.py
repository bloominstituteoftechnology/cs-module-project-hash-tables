"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

def function(a):
  if a <= 5:
   return a + 5
  elif 5 < a < 30:
   return a + 7
  else:
   return a * 100 

x = function(10)

print(x)

