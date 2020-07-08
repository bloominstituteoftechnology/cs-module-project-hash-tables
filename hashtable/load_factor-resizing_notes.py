Load Factor
-----------

The number of records in the hash table vs. the number of slots in the array


data = [None] * 32

put("1",99)
put("2",99)
put("3",99)
put("4",99)
put("5",99)
put("6",99)
put("7",99)
put("8",99)
put("9",99)
put("10",99)
put("11",99)
put("12",99)

load factor = 12 / 32 = 0.375

If the load is 1.0, we exactly the name number of data elements as array elements.

Resizing a hash table
---------------------

If the load > 0.7: resize

Resize:

* Make a new array with _double_ the capacity of the old one
* Have the hash table refer to that new array
* Run through all the nodes in the old hash table array
  * Put them in the new hash table array