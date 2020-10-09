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
        self.items = 0
        self.capacity = max(capacity, MIN_CAPACITY)
        self.hash_array = [None] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        print(self.items, '/', self.capacity)
        return self.items / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
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
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value, ha = None):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # self.hash_array[self.hash_index(key)] = value
        index = self.hash_index(key)
        working_array = ha if ha else self.hash_array
        if (working_array[index]) is not None:
            found = working_array[index].find(key)
            if found:
                found.value = value
            else:
                working_array[index].insert_at_head(HashTableEntry(key, value))
                self.items += 0 if ha else 1
        else:
            working_array[index] = LinkedList()
            working_array[index].insert_at_head(HashTableEntry(key, value))
            self.items += 0 if ha else 1

        # if self.get_load_factor() >= 0.7:
        #     self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.hash_array[index] is not None:
            found = self.hash_array[index].find(key)
            if found:
                found.value = None
                self.items -= 1
            else:
                print(f'Key "{key}" not found')

        # if self.get_load_factor() <= 0.2:
        #     self.resize(self.capacity // 2)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.hash_array[index] is not None:
            found = self.hash_array[index].find(key)
            if found:
                return found.value
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = max(MIN_CAPACITY, new_capacity)
        new_hash_array = [None] * self.capacity
        for item in self.hash_array:
            curr = item.head
            while curr is not None:
                self.put(curr.key, curr.value, new_hash_array)
                curr = curr.next

        self.hash_array = new_hash_array





# if __name__ == "__main__":
#     ht = HashTable(8)
#
#     ht.put("line_1", "'Twas brillig, and the slithy toves")
#     ht.put("line_2", "Did gyre and gimble in the wabe:")
#     ht.put("line_3", "All mimsy were the borogoves,")
#     ht.put("line_4", "And the mome raths outgrabe.")
#     ht.put("line_5", '"Beware the Jabberwock, my son!')
#     ht.put("line_6", "The jaws that bite, the claws that catch!")
#     ht.put("line_7", "Beware the Jubjub bird, and shun")
#     ht.put("line_8", 'The frumious Bandersnatch!"')
#     ht.put("line_9", "He took his vorpal sword in hand;")
#     ht.put("line_10", "Long time the manxome foe he sought--")
#     ht.put("line_11", "So rested he by the Tumtum tree")
#     ht.put("line_12", "And stood awhile in thought.")
#
#     print("")
#
#     # Test storing beyond capacity
#     for i in range(1, 13):
#         print(ht.get(f'line_{i}'))
#
#     # Test resizing
#     old_capacity = ht.get_num_slots()
#     ht.resize(ht.capacity * 2)
#     new_capacity = ht.get_num_slots()
#
#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")
#
#     # Test if data intact after resizing
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))
#
#     print("")

class LinkedList:

    def __init__(self):
        self.head = None

    def find(self, key):
        current_node = self.head
        while current_node is not None:
            if current_node.key == key:
                return current_node
            current_node = current_node.next

        return None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def delete(self, key):
        if key == self.head.ey:
            self.head = self.head.next
            return self.head

        prev = None
        curr = self.head

        while curr is not None:
            if curr.key == key:
                prev.next = curr.next
                return curr

            prev = curr
            curr = curr.next
        return None
