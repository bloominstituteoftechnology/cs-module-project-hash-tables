class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.key}: {self.value}\n"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class LinkedList:
    # singly linked list using HashTableEntry as a node class
    def __init__(self):
        self.head = None

    def __str__(self):
        text = ""
        current = self.head
        while current is not None:
            text += str(current)
            current = current.next
        return text

    def prepend(self, node):
        node.next = self.head
        self.head = node

    def append(self, node):
        current = self.head
        if current is None:
            self.prepend(node)
        else:
            while current.key == node.key or current.next is not None:
                if current.key == node.key:
                    current.value = node.value
                    return
                current = current.next
            current.next = node

    def find(self, key):
        cur = self.head
        while cur is not None:
            if cur.key == key:
                break
            cur = cur.next
        return cur

    def popleft(self):
        val = self.head
        if val is not None:
            self.head = val.next
        return val

    def delete(self, key):
        cur = self.head
        if cur.key == key:
            return self.popleft()
        if cur.next is None:
            return None
        prev = cur
        cur = prev.next
        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                return cur
            else:
                prev = cur
                cur = prev.next
        return None


class HashTable:
    """
    A hash table that with `capacity` buckets that accepts string keys

    Each bucket is a singly linked list in order to handle collision
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity if capacity >= MIN_CAPACITY else MIN_CAPACITY
        self.list = [LinkedList() for _ in range(self.capacity)]
        self.count = 0

    def __str__(self):
        text = ""
        for i in range(len(self.list)):
            text += f"Bucket {i}:\n"
            text += str(self.list[i])
            text += "\n"
        return text

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
        hash_val = 14695981039346656037
        for char in key:
            hash_val = hash_val * 1099511628211
            hash_val = hash_val ^ ord(char)
        return hash_val

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash_val = 5381
        for char in key:
            hash_val = ((hash_val << 5) + hash_val) + ord(char)
        return hash_val & 0xFFFFFFFF

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
        # Your code here
        # print(self.hash_index(key), key, value)
        self.count += 1
        # current = self.list[self.hash_index(key)]
        # if self.list[self.hash_index(key)]:
        #     while current.next is not None or current.key == key:
        #         if current.key == key:
        #             current.value = value
        #             return
        #         current = current.next
        #     current.next = HashTableEntry(key, value)
        # else:
        #     self.list[self.hash_index(key)] = HashTableEntry(key, value)

        bucket = self.list[self.hash_index(key)]
        bucket.append(HashTableEntry(key, value))
        # if self.get_load_factor() > .7:
        #     self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        self.count -= 1
        # index = self.hash_index(key)
        # if self.list[index]:
        #     current = self.list[index]
        #     while current.next is not None:
        #         if current.next.key == key:
        #             # remove the node
        #             break
        #         current = current.next
        #     return current.value
        # else:
        #     return None
        bucket = self.list[self.hash_index(key)]
        bucket.delete(key)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # if self.list[self.hash_index(key)]:
        #     bucket = self.list[self.hash_index(key)]
        #     while bucket is not None:
        #         if bucket.key == key:
        #             return bucket.value
        #         bucket = bucket.next
        bucket = self.list[self.hash_index(key)]
        val = bucket.find(key)
        if val is None:
            return None
        return bucket.find(key).value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        data = self.list
        # self.list = [LinkedList()] * new_capacity
        # self.capacity = new_capacity
        # self.count = 0
        self.__init__(new_capacity)
        for bucket in data:
            current = bucket.head
            while current is not None:
                self.put(current.key, current.value)
                current = current.next


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
