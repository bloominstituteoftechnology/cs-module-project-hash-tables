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
        # Your code here
        self.capacity = capacity if capacity >= MIN_CAPACITY else MIN_CAPACITY
        self.count = 0
        self.list = [None] * self.capacity


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
        return self.count / self.capacity


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
        for val in key:
            hash = ((hash << 5) + hash) + ord(val)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if not self.list[index]:
            self.list[index] = HashTableEntry(key, value)
            self.count += 1
            if self.count == self.capacity - 1:
                self.resize()
        elif self.list[index].key == key:
            self.list[index].value = value
        else:
            current = self.list[index]
            while current.next:
                current = current.next
            if not current.next:
                print("We in here boys")
                current.next = HashTableEntry(key, value)
                self.count += 1
                if self.count == self.capacity - 1:
                    self.resize()


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        n = self.list[index]
        if not n:
            print("Couldn't find value to remove")
            return

        if not n.next:
            if n.key == key:
                self.list[index] = None
                self.count -= 1
            else:
                print("Couldn't find value to remove")
        else:
            current = n
            previous = None
            if current.key == key:
                self.list[index] = current.next
                self.count -= 1
            else:
                while current.next:
                    previous = current
                    current = current.next
                    if current.key == key:
                        previous.next = current.next
                        self.count -= 1
                        return
                print("Couldn't find a value to remove")




    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.list[index]:
            n = self.list[index]
            if n.key == key:
                return n.value
            elif n.next:
                current = n
                while current.next:
                    if current.key == key:
                        return current.value
                    current = current.next
        print("Could not find value")
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity *= 2
        old_list = self.list
        self.list = [None] * self.capacity
        for item in old_list:
            if item.next:
                current = item
                while True:
                    if current.next: break




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
