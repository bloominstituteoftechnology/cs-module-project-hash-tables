# Hash Tables

## Day 1

Task: Implement a basic hash table without collision resolution.

1. Implement a `HashTable` class and `HashTableEntry` class.

2. Implement a good hashing function.

   Recommend either of:

   * DJB2
   * FNV-1 (64-bit)

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

