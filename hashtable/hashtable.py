from linked_list import LinkedList

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


def DJB2(key):
    hash = 5381
    for i in key:
        hash = (hash + 33) + ord(i)
    return hash  # and 0xFFFFFFFF


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [LinkedList()] * capacity
        self.number_of_records = 0
        # self.data = [None] * capacity
        # self.load = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # return self.load / self.capacity
        return self.number_of_records / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for i in key:
            hash = (hash + 33) + ord(i)
        return hash  # and 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        cur = self.storage[index].head
        
        while cur:
            if cur.key == key:
                cur.value = value

            cur = cur.next

        entry = HashTableEntry(key, value)
        self.storage[index].insert_at_head(entry)
        self.number_of_records += 1
        
        # index = self.hash_index(key)
        # if self.data[index] == None:
        #     self.data[index] = HashTableEntry(key, value)
        #     self.load += 1

        # else:
        #     node = self.data[index]
        #     if node.key == key:
        #         node.value = value

        #     else:
        #         while node.next != None and node.key != key:
        #             node = node.next
        #         node.next = HashTableEntry(key, value)
        #         self.load += 1

        # if self.get_load_factor() > 0.7:
        #     self.resize(self.capacity * 2)
        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        self.put(key, None)
        self.number_of_records -= 1
        
        # index = self.hash_index(key)
        # if self.data[index] == None:
        #     print("Error: Key not found")

        # elif self.data[index].key == key:
        #     self.data[index] = None
        #     self.load -= 1

        # elif (self.data[index].key != key) and (self.data[index].next != None):
        #     prev = self.data[index]
        #     curr = self.data[index].next

        #     while curr.key != key and curr.next != None:
        #         prev, curr = curr, curr.next

        #     if curr.key == key:
        #         prev.next = curr.next
        #         self.load -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        # Your code here
        index = self.hash_index(key)
        cur = self.storage[index].head

        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next

        return None
        
        # index = self.hash_index(key)
        # node = self.data[index]
        # if node == None:
        #     return node

        # while node.key != key and node.next != None:
        #     node = node.next

        # if node.key == key:
        #     return node.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        if self.get_load_factor() >= 0.7:
            old_storage = self.storage
            self.storage = [LinkedList()] * new_capacity
            for record in old_storage:
                cur = record.head
                while cur:
                    self.put(cur.key, cur.value)
                    cur = cur.next
                    
            self.capacity = new_capacity
        
        # old_data = self.data
        # self.data = [None] * new_capacity
        # self.capacity = new_capacity
        # self.load = 0

        # for item in old_data:
        #     while item:
        #         self.put(item.key, item.value)
        #         item = item.next


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
