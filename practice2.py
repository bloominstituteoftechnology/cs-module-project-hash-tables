# Can we build something that helps us search faster?
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

def print_departments(dep_name):
  results = []
  #search through our list of records iterate through the entire list
  #  if value == engineering add to our results list
  return results

def build_index(records):
  idx = {}
  # Build a dict where the keys are: department
  # the values are: list of names
  #loop through the records at least once
  for record in records:
    name = record[0]
    department = record[1]
    # the department might not exist yet in the dictionary
    if department not in idx:
      idx[department] = [name]
    else:
      idx[department].append(name)
  return idx    

index_dict = build_index(records) 
def print_department_using_index(dep_name):
  return index_dict[dep_name]

# print everyone in Engineering using the print_department
#  print_department("Engineering")  

# print everyone in Engineering uisng dict
results = print_department_using_index("Engineering")
print(results)