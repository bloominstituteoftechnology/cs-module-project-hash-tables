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
        if capacity >= MIN_CAPACITY:
            self.capacity = capacity
        else:
            self.capacity = MIN_CAPACITY
        self.bucket = [None] * capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.bucket)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.get_num_slots()

    def fnv1(self, key):
         prime_32 = 16777619
         hash_32 = 2166136261
         fnv_prime_64 = 1099511628211  # (in hex: 0x100000001b3)
         hash_64 = 14695981039346656037  # (in hex: 0xcbf29ce484222325)

        for char in key:
            hash_64 = hash_64 * fnv_prime_64
            hash_64 = hash_64 ^ ord(char)
        return hash

    def djb2(self, key):
        hash = 5381
        for x in key:
            # shift variable, then add it, then add the ord
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xffffffff

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        # first_day
        # index = self.hash_index(key)
        # self.bucket[index] = value

        # second_day
        index = self.hash_index(key)  # returns a number
        new_node = HashTableEntry(key, value)  # returns a node Object
        cur_node = self.bucket[index]  # returns node Object or None
        if self.bucket[index] == None:
            # if node at index does NOT exist, then insert new_node at index
            self.bucket[index] = new_node
            self.count += 1
        elif self.bucket[index] is not None and self.bucket[index].key == key:
            # if node at index exists, and node.key matches key, replace value at key
            self.bucket[index].value = value

        elif self.bucket[index] is not None:
            # if node at index exits...
            while cur_node is not None:
                # loop while cur_node exists...
                if cur_node.next is None:
                    # ...if next node is None, then insert node into next index
                    cur_node.next = new_node
                    self.count += 1
                    return cur_node
                elif cur_node.next is not None and cur_node.next.key == key:
                    # ...if next node exists, and next node.key matches, replace value
                    cur_node.next.value = value
                    return cur_node.next
                else:
                    # move over to next node, run through the loop again
                    cur_node = cur_node.next




    def delete(self, key):
        # first_day
        # index = self.hash_index(key)
        # self.bucket[index] = None

        
        # second_day
        index = self.hash_index(key)  # returns a number
        is_traversing = True
        cur_node = self.bucket[index]  # returns a node Object
        prev_node = None

        while is_traversing:
            # while is_traversing is true
            if cur_node.key:
                # ...if current node key exists
                if cur_node.key == key:
                    # ...if current node key matches, set current to none
                    cur_node.value = None
                if cur_node.next:
                    # ...if next node exists, set current node to next node
                     self.bucket[index] = cur_node.next
                     cur_node = cur_node.next
                else:
                    self.bucket[index] = None
                    cur_node = None
            else:
                return "Error"

        

    def get(self, key):
        # first_day
        # index = self.hash_index(key)
        # return self.bucket[index]

        # second_day
        index = self.hash_index(key)
        cur_node = self.bucket[index]

        # if cur_node exists, and the key matches node key: return the node value
        if cur_node is not None and cur_node.key == key:
            return cur_node.value
        else:
            while cur_node is not None:
                if cur_node.key == key:
                    return cur_node.value
                cur_node = cur_node.next

        return None



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        oldBucket = self.bucket
        # create a new, empty bucket with new_capacity length
        self.bucket = [None] * new_capacity
        self.count = 0
        self.capacity = new_capacity
        index = 0

        while index < len(oldBucket):
            cur_node = oldBucket[index]

            if cur_node is not None:
                next_node = cur_node.next
                cur_node.next = None
                self.put(cur_node.key, cur_node.value)
                oldBucket[index] = next_node
            elif cur_node is None:
                # index ONLY increments when cur_node is None
                index += 1





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
