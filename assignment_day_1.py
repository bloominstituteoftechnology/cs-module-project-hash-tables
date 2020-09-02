country_code = {'25': 'USA', '20': 'India', '10': 'Nepal'}
print (country_code['10'])
print (country_code['20'])

country_code = [('25', 'USA'), ('20', 'India'), ('10', 'Nepal')]
def insert(item_list, key, value):
    item_list.append((key, value))

def search(item_list, key):
    for item in item_list:
        if item[0] == key:
            return item[1]

print (search(country_code, '20'))




hash_table = [None] * 10
print (hash_table)

def hashing_fun(key):
    return key % len(hash_table)

print (hashing_fun(10))
print (hashing_fun(20))
print (hashing_fun(25))

def insert(hash_table, key, value):
    hash_key = hashing_fun(key)
    hash_table[hash_key] = value

insert(hash_table, 10, 'Nepal')
print (hash_table)

insert(hash_table, 25, 'USA')
print (hash_table)

### Collision

insert(hash_table, 20, 'India')
print (hash_table)

### the result of hashing_func for keys 10 and 20 is the same 


### Collision Resolution 
### There are generally two ways to resolve a collision: 1. Linear Probing 2. Chaining

## Linear Probing


## Chaining

hash_table =[[] for _ in range(10)]
print (hash_table)

def hashing_func(key):
    return key % len(hash_table)

print (hashing_func(10))
print (hashing_func(20))
print (hashing_func(25))

def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    hash_table[hash_key].append(value)

insert(hash_table, 10, 'Nepal')
print (hash_table)

insert(hash_table, 25, 'USA')
print (hash_table)

insert(hash_table, 20, 'India')

## Standard implementation

hash_key = hash('xyz')
print(hash_key)

hash_key = hash('10')
print(hash_key)

hash_key = hash(10)
print(hash_key)

hash_key = hash('20')
print(hash_key)

hash_key = hash(10)
print(hash_key)

hash_key = hash('25')
print(hash_key)

hash_key = hash(25)
print(hash_key)

hash_key = hash('10') % len(hash_table)
print(hash_key)

hash_key = hash('20') % len(hash_table)
print(hash_key)

hash_key = hash('25') % len(hash_table)
print(hash_key)

hash_key = hash(10) % len(hash_table)
print(hash_key)

hash_key = hash(20) % len(hash_table)
print(hash_key)

hash_key = hash(25) % len(hash_table)
print(hash_key)


#empty hash table
hash_table = [[] for _ in range(10)]
print(hash_table)

## insert data into table
def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = Falsebucket = hash_table[hash_key]
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))

insert(hash_table, 10, 'Nepal')
insert(hash_table, 25, 'USA')
insert(hash_table, 20, 'India')
print(hash_table)

#search data from hash table
def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v

print(search(hash_table, 10))
print(search(hash_table, 20))
print(search(hash_table, 30))


## Delete data from Hash Table

def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            del bucket[i]
            print('Key {} deleted'.format(key))
        else:
            print('key {} not found'.format(key))

delete(hash_table, 10)
print(hash_table)