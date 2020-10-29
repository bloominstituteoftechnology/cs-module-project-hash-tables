# Hash Tables

## Day 1

Task: Implement a basic hash table without collision resolution.

1. Implement a `HashTable` class and `HashTableEntry` class.

2. Implement a good hashing function.

   Recommend either of:

   * DJB2 - research
"""
   def hash_djb2(s):                                                                                                                                
    hash = 5381
    for x in s:
        hash = (( hash << 5) + hash) + ord(x)
    return hash & 0xFFFFFFFF


hex(hash_djb2(u'something'))
"""
   * FNV-1 (64-bit) - BIG RESEARCH

   core:
      hash = offset_basis
      for each octet_of_data to be hashed
         hash = hash * FNV_prime
         hash = hash xor octet_of_data
      return hash

   alt:
      hash = offset_basis
      for each octet_of_data to be hashed
         hash = hash xor octet_of_data
         hash = hash * FNV_prime
      return hash

   Parameter for 64-bit:
      64 bit FNV_prime = 240 + 28 + 0xb3 = 1099511628211

   Offset Basis: (dependent on n, the size of the hash)
      64 bit offset_basis = 14695981039346656037

[https://stackoverflow.com/questions/50542882/create-minimum-perfect-hash-for-sparse-64-bit-unsigned-integer]

[https://github.com/sup/pyhash/blob/master/pyhash/pyhash.py]

[https://github.com/sup/pyhash]

   You are allowed to Google for these hashing functions and implement
   from psuedocode.

3. Implement the `hash_index()` that returns an index value for a key.

4. Implement the `put()`, `get()`, and `delete()` methods.

You can test this with:

```
python test_hashtable_no_collisions.py
```

The above test program is _unlikely_ to have collisions, but it's
certainly possible for various hashing functions. With DJB2 (32 bit) and
FNV-1 (64 bit) hashing functions, there are no collisions.

## Day 2

Task: Implement linked-list chaining for collision resolution.

1. Modify `put()`, `get()`, and `delete()` methods to handle collisions.

2. There is no step 2.

You can test this with:

```
python test_hashtable.py
```

Task: Implement load factor measurements and automatic hashtable size
doubling.

1. Compute and maintain load factor.

2. When load factor increases above `0.7`, automatically rehash the
   table to double its previous size.

   Add the `resize()` method.

You can test this with both of:

```
python test_hashtable.py
python test_hashtable_resize.py
```

Stretch: When load factor decreases below `0.2`, automatically rehash
the table to half its previous size, down to a minimum of 8 slots.

## Day 3 and Day 4

Work on the hashtable applications directory (in any order you
wish--generally arranged from easier to harder, below).

For these, you can use either the built-in `dict` type, or the hashtable
you built. (Some of these are easier with `dict` since it's more
full-featured.)

* [Lookup Table](applications/lookup_table/)
* [Expensive Sequence](applications/expensive_seq/)
* [Word Count](applications/word_count/)
* [No Duplicates](applications/no_dups/)
* [Markov Chains](applications/markov/)
* [Histogram](applications/histo/)
* [Cracking Caesar Ciphers](applications/crack_caesar/)
* [Sum and Difference](applications/sumdiff/)

