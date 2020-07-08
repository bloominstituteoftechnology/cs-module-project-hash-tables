Slot
Index Chain (linked list)
----- -------------------------------
 0    -> ("qux",10) -> None
 1    -> ("plugh",20) -> ("foo",55) -> None
 2    -> ("xyzzy",50) -> ("baz",999) -> ("bar",30) -> None
 3    -> None

put("foo", 12)
put("bar", 30)
put("baz", 999)
put("qux", 10)
put("plugh", 20)
put("xyzzy", 50)
put("foo", 55)

get("baz")

Hash function results
---------------------
"foo" -> 1
"bar" -> 2
"baz" -> 2 -- collision!
"qux" -> 0
"plugh" -> 1 -- collision!
"xyzzy" -> 2 -- collision!

Pseudocode for put
------------------
* Find the index in the hash table for the key
* Search the list at that index for the key
* If it exists:
  * Overwrite the value
* Else it doesn't exist:
  * Make a new record (`HashTableEntry` class) with the key and value
  * Insert it anywhere in the list

Pseudocode for get
------------------
* Find the index in the hash table for the key
* Search the list at that index for the key
* If it exists:
  * Return the value
* Else it doesn't exist:
  * Return `None`

Pseudocode for delete
---------------------
* Find the index in the hash table for the key
* Search the list at that index for the key
* If it exists:
  * Delete the entry from the linked list
  * Politely return the deleted value
* Else it doesn't exist:
  * Return `None`

Linked list node
----------------

class HashTableEntry:   # Node in the linked list
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None   # Make this a linked list node