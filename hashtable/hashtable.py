class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.item_count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.item_count/self.capacity
        


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        hash = 5381
        byte_array = key.encode('utf-8')
        for byte in byte_array:
            hash = ((hash * 33) ^ byte) % 0x100000000
        return hash 


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        key_hash = self.djb2(key)
        bucket_index = key_hash % self.capacity

        new_node = HashTableEntry(key, value)
        existing_node = self.storage[bucket_index]

        if existing_node:
            last_node = None
            while existing_node:
                if existing_node.key == key:
                    # if an exsiting key is found, replace the value 
                    existing_node.value = value
                    return 
                last_node = existing_node
                existing_node = existing_node.next
                #if we get this far, we didnt find any exisiting key, so just append the new node to the end of the bucket
            last_node.next = new_node
        else:
            self.storage[bucket_index] = new_node

    def delete(self, key):
        key_hash = self.djb2(key)
        bucket_index = key_hash % self.capacity

        existing_node = self.storage[bucket_index]
        if existing_node:
            last_node = None
            while existing_node:
                if existing_node.key == key:
                    if last_node:
                        last_node.next = existing_node.next
                    else:
                        self.storage[bucket_index] = existing_node.next
                last_node = existing_node
                existing_node = existing_node.next
        else:
            print("Not found!")




    def get(self, key):
        key_hash = self.djb2(key)
        bucket_index = key_hash % self.capacity

        existing_node = self.storage[bucket_index]
        if existing_node:
            while existing_node:
                if existing_node.key == key:
                    return existing_node.value
                existing_node = existing_node.next

        return None


    def resize(self, new_capacity):
        if new_capacity >= self.capacity:
            self.capacity = new_capacity
            difference = new_capacity - len(self.storage) 
            self.storage.append()
            for x in self.storage:
                self.djb2(x.key)
            return self.storage
        else:
            return ("I dont know how to make it smaller!")


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
