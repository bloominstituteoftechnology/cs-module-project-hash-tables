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
        if capacity < MIN_CAPACITY:
            capacity = MIN_CAPACITY
        self.capacity = capacity
        self.count = 0
        self.array = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


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
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


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
        self.count += 1
        load_factor = self.count / self.capacity
        if load_factor > 0.8:
            print("need to resize")
            self.resize(self.capacity * 2)


        # get the index in the hash table for the key
        index = self.hash_index(key)

        # create node with key, value
        hte = HashTableEntry(key, value)

        # check hash table for a linked list
        if self.array[index] is not None:
            cur = self.array[index]

            prev = cur

            while cur is not None:
                if cur.key == key:
                    prev.next = hte
                    self.delete(key)
                    # cur = hte
                    self.print_me("PUT (EARLY EXIT)", key)
                    return
                else:
                    prev = cur
                    cur = cur.next
            prev.next = hte
        else:
            self.array[index] = hte


        self.print_me("PUT", key)

    def print_me(self, type, key):
        print("\nHASH TABLE\n----------")
        print("Function Type: ", type, key)
        counter = 0
        for item in self.array:
            if item is not None:
                cur = item
                string = ""
                while cur is not None:
                    string += cur.key
                    string += ", "
                    string += cur.value
                    string += " -> "
                    # print(counter, ":", cur.key, cur.value)
                    cur = cur.next
                string += "None"
                print(counter, ":", string)
            else:
                print(counter, ":", item)
            counter += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        # self.array[index] = None

        if self.array[index] is not None:
            cur = self.array[index]
            # special case of deleting the head
            if cur.key == key:
                if cur.next is not None:
                    cur = cur.next
                    self.array[index] = cur
                    # cur.next = None
                else:
                    self.array[index] = None
                self.print_me("DELETE (EARLY EXIT) w/ KEY:", key)
                return cur

            prev = cur
            cur = cur.next

            while cur is not None:
                if cur.key == key:
                    prev.next = cur.next  # cuts out the node from the list
                    cur.next = None
                    return cur
                else:
                    prev = prev.next
                    cur = cur.next
            self.print_me("DELETE w/ KEY:", key)
            return None
        else:
            return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        index = self.hash_index(key)

        if self.array[index] is not None:
            cur = self.array[index]

            while cur is not None:
                if cur.key == key:
                    return cur.value
                cur = cur.next
        else:
            return None

        # return self.array[index].value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.print_me("RESIZE BEFORE W/ CAPACITY", self.capacity)
        new = [None] * new_capacity

        counter = 0
        for item in self.array:
            new[counter] = item
            counter += 1

        self.array = new

        self.print_me("RESIZE AFTER W/ NEW_CAPACITY", new_capacity)



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
