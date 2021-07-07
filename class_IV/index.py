records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing")
]

# Which employees are in a given department?

dept_idx = {}

# Build index by dept
for name, dept in records: # O(n) over number of records
    if dept not in dept_idx:
        dept_idx[dept] = []

    dept_idx[dept].append(name)

print(dept_idx)

def emp_by_dept(d):
    # emp = []

    # for name, dept in records: # O(n)
    #     if dept == d:
    #         emp.append(name)

    return dept_idx[d] # O(1)

def add_employee(name, dept):
    """Maintain the index"""

    records.append((name, dept))

    if dept not in dept_idx:
        dept_idx[dept] = []

    dept_idx[dept].append(name)

print(emp_by_dept("Sales"))

add_employee("Hank", "Marketing")

print(emp_by_dept("Marketing"))