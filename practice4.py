#fib
import math
# 1.Memoization in python
cache = {}
def fib(n):
  if n<=1:
    return n
  # if the results in the cache then return it  
  if n in cache:
    return cache[n]
  # if the results is not in the cache do the expensive calculations.  
  result = fib(n-1)+fib(n-2)
  #Store the result from the expensive calculations.
  cache[n] = result

  return result

# print(fib(5))    
# print(fib(15))
# print(cache)

# 2.Lookup table: 
# if we have something expensive to do..we can use lookup tables
# but these operations repeat and we know most common inputs now.
sqrt_table = {}
def compute_inverse_square(n):
  result = 1/math.sqrt(n)
  return result

def build_lookup_table():
  for i in range(1,1000):
    sqrt_table[i]=compute_inverse_square(i)

build_lookup_table()

def faster_compute_square(n):
  return sqrt_table[n]    

r = faster_compute_square(179)
# print(r)
# print(sqrt_table)

# 3.indexing:-
records = [
  ('alice', 'maths'),
  ('Dave', 'Engineering'),
  ('john', 'science'),
  ('bob','science'),
  ('David', 'Engineering'),
  ('grace', 'romance'),
  ('frank', 'Marketing'),
  ('Phil', 'Engineering')
]

def print_department(dep_name):
  results=[]
  # search through our list of records
  for record in records:
    name = record[0]
    department = record[1]
    if department == 'Engineering':
      results.append(name)
  #iterate through the entire list    
    # if value as engineering and to our results list
  return results

total_results = print_department('Engineering')    
# print(total_results)

def build_index(records):
  idx = {}
  for record in records:
    name = record[0]
    department = record[1]
    if department in idx:
      idx[department].append(name)
    else:
      idx[department] = [name]
  return idx


index_dict = build_index(records)

def print_department_using_index(dep_name):
  print(index_dict[dep_name])

print_department_using_index('Engineering')




  