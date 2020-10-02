class HashTableEntry - Linked List hash table containing linked lists of key value pairs. "Node".

class HashTable - A hash table that with `capacity` buckets that accepts string keys. 

    get num slots - Return the length of the list you're using to hold the hash table data. (Not the number of items stored in the hash table, but the number of slots in the main list.) One of the tests relies on this.

    get load factor - Return the load factor for this hash table.

    fnv1 - hash algorithm 64 bit

    djb2 - DJB2 hash, 32-bit, no implemented

    hash index - Take an arbitrary key and return a valid integer index between within the storage capacity of the hash table.

    put - Store the value with the given key. Hash collisions should be handled with Linked List Chaining.]

    delete - Remove the value stored with the given key. Print a warning if the key is not found.

    get - Retrieve the value stored with the given key. Returns None if the key is not found.

    resize - Changes the capacity of the hash table and rehashes all key/value pairs.

