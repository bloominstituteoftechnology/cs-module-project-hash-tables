class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        currStr = ''
        curr = self.head
        while curr != None:
            currStr += f'{str(curr.value)} -> '
            curr = curr.next
        return currStr + 'None'

    # return node w/ value
    def find(self, value):
        curr = self.head
        while curr != None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    # deletes node w/ given value then returns that node
    def delete(self, value):
        curr = self.head
        prev = None

        # special case to delete head
        if curr.value == value:
            self.head = curr.next
            curr.next = None
            return curr

        while curr != None:
            if curr.value == value:
                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next
    
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    # overwrite node or insert node at head
    def insert_at_head_or_overwrite(self, node):
        existingNode = self.find(node.value)
        if existingNode != None:
            existingNode.value = node.value
            return False
        else:
            self.insert_at_head(node)
            return True

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __eq__(self, other):
        if isinstance(other, HashTableEntry):
            return self.key == other.key
        return False


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = max(MIN_CAPACITY, capacity)
        self.count = 0
        self.table = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hval = 0x811c9dc5
        fnv_32_prime = 0x01000193
        uint32_max = 2 ** 32
        for s in key:
            hval = hval ^ ord(s)
            hval = (hval * fnv_32_prime) % uint32_max
        return hval


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for char in key:
            hash = ((hash << 5) + hash) + ord(char)
        return hash & 0xFFFFFFFF


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
        hash_index = self.hash_index(key)
        if self.table[hash_index] != None:
            linked_list = self.table[hash_index]
            did_add_new_node = linked_list.insert_at_head_or_overwrite(Node(HashTableEntry(key, value)))
            if did_add_new_node:
                self.count += 1
        else:
            linked_list = LinkedList()
            linked_list.insert_at_head(Node(HashTableEntry(key, value)))
            self.table[hash_index] = linked_list
            self.count += 1
        if self.get_load_factor() > 0.7:
            self.resize(self.get_num_slots() * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hash_index = self.hash_index(key)
        if self.table[hash_index] != None:
            linked_list = self.table[hash_index]
            did_delete_node = linked_list.delete(HashTableEntry(key, None))
            if did_delete_node != None:
                self.count -= 1
                if self.get_load_factor() < 0.2:
                    self.resize(max(self.get_num_slots() / 2, MIN_CAPACITY))
        else:
            print('WARNING! Node not found')


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hash_index = self.hash_index(key)
        if self.table[hash_index] != None:
            linked_list = self.table[hash_index]
            node = linked_list.find(HashTableEntry(key, None))
            if node != None:
                return node.value.value
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_table = self.table
        self.table = [None] * int(new_capacity)
        # self.count = 0

        for element in old_table:
            if element == None:
                continue
            curr_node = element.head
            while curr_node != None:
                temp = curr_node.next
                curr_node.next = None
                hash_index = self.hash_index(curr_node.value.key)

                if self.table[hash_index] != None:
                    self.table[hash_index].insert_at_head(curr_node)
                else:
                    linked_list = LinkedList()
                    linked_list.insert_at_head(curr_node)
                    self.table[hash_index] = linked_list
                
                curr_node = temp
                # self.count += 1



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
