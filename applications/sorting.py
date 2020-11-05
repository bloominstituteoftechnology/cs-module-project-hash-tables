d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}​

items = list(d.items())​

# Sort ascending by key
items.sort()​

for i in items:
    print(f'{i[0]}: {i[1]}')    

# Sort ascending by value​

#def keyfunc(e):
#    return e[1]
#items.sort(key=keyfunc)​

items.sort(key=lambda e: e[1])​

for i in items:
    print(f'{i[0]}: {i[1]}')