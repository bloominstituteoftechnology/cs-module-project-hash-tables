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

# ? Different strategies for handling collisions:
# ? - Chaining: array of linked lists with 1 LL per index, each node.next points to second element
# ? - Array of arrays, with one array per index, just append
# ? - Disallow collisions
# ? - Open addressing. Linear probing, quadratic probing. [None, 'hello', 'world', None]


class HashTable:
    # ? A hash table that with `capacity` buckets
    # ? that accepts string keys

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.load = 0

    def get_num_slots(self):
        # ? Return the length of the list you're using to hold the hash
        # ? table data. (Not the number of items stored in the hash table,
        # ? but the number of slots in the main list.)

        return len(self.storage)

    def get_load_factor(self):
        # ? Return the load factor for this hash table.
        return self.load / self.capacity

    def fnv1(self, key):
        # ? FNV-1 Hash, 64-bit
        # ? Implement this, and/or DJB2.
        pass

    # * Visualization of djb2:
    # * http://pythontutor.com/visualize.html#code=def%20djb2%28key%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20DJB2%20hash,%2032-bit%0A%0A%20%20%20%20%20%20%20%20Implement%20this,%20and/or%20FNV-1.%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20hash%20%3D%205381%0A%20%20%20%20%20%20%20%20for%20x%20in%20key%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20hash%20%3D%20%28%28hash%20%3C%3C%205%29%20%2B%20hash%29%20%2B%20ord%28x%29%0A%20%20%20%20%20%20%20%20return%20hash%20%26%200xFFFFFFFF%0A%20%20%20%20%20%20%20%20%0Adjb2%28%22hello%22%29&cumulative=false&curInstr=16&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
    def djb2(self, key):
        # ? DJB2 hash, 32-bit
        # ? Implement this, and/or FNV-1.
        hash = 5381  # ? The hash value, for this hashing algoritm it will always start as 5381
        for x in key:  # ? For every letter in 'key'
            hash = ((hash << 5) + hash) + ord(x)
            # ? For each letter, hash gets set to
            # ? ()
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        # ? Take an arbitrary key and return a valid integer index
        # ? between within the storage capacity of the hash table.

        # ! return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        # ? Store the value with the given key.
        # ? Hash collisions should be handled with Linked List Chaining.

        idx = self.hash_index(key)
        node = self.storage[idx]
        new_node = HashTableEntry(key, value)

        if self.storage[idx] != None:

            if node.key == key:
                node.value = value
            else:
                while node.next is not None:
                    if node.next.key == key:
                        node.next.value = value
                        break
                    else:
                        node = node.next

                node.next = new_node
        else:
            self.storage[idx] = new_node

        self.load += 1
        

    def delete(self, key):
        # ? Remove the value stored with the given key.
        # ? Print a warning if the key is not found.

        # ? Delete: find the value, then set to None
        idx = self.hash_index(key)
        node = self.storage[idx]

        if node is None:
            print(f"The key '{key}' does not exist.'")
        elif node.key == key:
            node.key = None
            self.load -= 1
        else:
            prev_node = node
            curr_node = prev_node.next

            while curr_node is not None:
                if curr_node.key == key:
                    curr_node.key = None
                    break
                else:
                    prev_node = curr_node
                    curr_node = curr_node.next
            self.load -= 1

        # idx = self.hash_index(key)

        # if self.storage[idx] is None:
        #     print(f"The key '{key}' does not exist.'")
        # elif self.storage[idx].next is None:
        #     self.storage[idx] = None
        #     self.load -= 1
        # else:
        #     prev_node = self.storage[idx]
        #     curr_node = prev_node.next

        #     while curr_node is not None:
        #         if curr_node.key == key:
        #             prev_node.next = curr_node.next
        #         else:
        #             prev_node = curr_node
        #             curr_node = curr_node.next
        #     self.load -= 1

    def get(self, key):
        # ? Retrieve the value stored with the given key.
        # ? Returns None if the key is not found.

        # ? Get
        # ? 1. Hash our string/key, string --> number
        # ? 2. Mod this number by length of array
        # ? 3. Use this modded number / index to get the value there

        idx = self.hash_index(key)
        node = self.storage[idx]

        if node is None:
            print(f"The key '{key}' does not exist.'")
        else:
            while node is not None:
                # check for the target value
                if node.key == key:
                    print(f" | {node.key}, {node.value} | ")
                    return node.value
            # move to next node
                else:
                    node = node.next

    def resize(self, new_capacity=None):
        # ? Changes the capacity of the hash table and
        # ? rehashes all key/value pairs.

        if self.get_load_factor() > 0.7:
            if new_capacity is None:
                new_capacity = self.capacity * 2

            old_storage = self.storage
            self.storage = [None] * new_capacity

            for node in old_storage:
                if node is not None:
                    self.put(node.key, node.value)

                    curr_node = node
                    while curr_node.next is not None:
                        self.put(curr_node.next.key, curr_node.next.value)
                        curr_node = curr_node.next
        elif self.get_load_factor() < 0.2:
            if new_capacity is None and self.capacity / 2 >= 8:
                new_capacity = self.capacity / 2
            else:
                new_capacity = 8

            old_storage = self.storage
            self.storage = [None] * new_capacity

            for node in old_storage:
                if node is not None:
                    self.put(node.key, node.value)

                    curr_node = node
                    while curr_node.next is not None:
                        self.put(curr_node.next.key, curr_node.next.value)
                        curr_node = curr_node.next


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
