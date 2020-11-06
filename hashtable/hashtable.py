# from linked_list import LinkedList


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


class LinkedList:
    def __init__(self):
        self.head = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [LinkedList()] * capacity
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

        return len(self.data)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / len(self.capacity)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hashed = 0xCBF29CE484222325
        fnv_prime = 0x100000001b3

        for byte in key.encode():
            hashed *= byte
            hashed ^= byte

        return hashed

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # turn the key in to a string and get its bytes
        str_key = str(key).encode()

        # start from an abitary large prime
        hash_value = 5381

        # loop over the str_key extracting the byte (b)
        for b in str_key:
            hash_value = ((hash_value << 5) + hash_value) + b
            hash_value &= 0xFFFFFFFF

        return hash_value

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        slot = self.hash_index(key)

        # if LL is empty
        if self.data[slot].head == None:
            self.data[slot].head = HashTableEntry(key, value)
            self.count += 1
            return

        else:
            curr = self.data[slot].head

            while curr.next:

                if curr.key == key:
                    curr.value = value
                curr = curr.next

            curr. next = HashTableEntry(key, value)
            self.count += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)
        curr = self.data[slot].head

        if curr.key == key:
            self.data[slot].head = self.data[slot].head.next
            self.count -= 1
            return

        while curr.next:
            prev = curr
            curr = curr.next
            if curr.key == key:
                prev.next = curr.next
                self.count -= 1
                return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)

        curr = self.data[slot].head

        if curr == None:
            return None

        if curr.key == key:
            return curr.value

        while curr.next:
            curr = curr.next
            if curr.key == key:
                return curr.value
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity
        new_list = [LinkedList()] * new_capacity

        for i in self.data:
            curr = i.head

            while curr is not None:
                slot = self.hash_index(curr.key)

                if new_list[slot].head == None:
                    new_list[slot].head = HashTableEntry(curr.key, curr.value)
                else:
                    node = HashTableEntry(curr.key, curr.value)

                    node.next = new_list[slot].head

                    new_list[slot].head = node
                curr = curr.next
            self.storage = new_list


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
