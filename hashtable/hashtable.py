class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
	    return f'HashTableEntry({repr(self.value)})'

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity

    def get_num_slots(self):
        return len(self.table)

    def count_at_index(self, index):
        count = 0
        if self.table[index] is None:
            return count
        else:
            current = self.table[index]
            while current is not None:
                next = current.next
                count += 1
                current = next
            return count

    def get_load_factor(self):
        load = 0
        for index in self.table:
            if index is None:
                continue
            else:
                load += self.count_at_index(index)
        return load / self.capacity

    def fnv1(self, key):
        k = str(key).encode()
        hash = 0
        offset_basis = 14695981039346656037
        prime = 1099511628211
        size = 2**64

        for byte in k:
            hash = (offset_basis * prime) % size
            hash = hash ^ byte
            hash &= 0xffffffffffffffff

        return hash

    # def djb2(self, key):
        # Your code here

    def hash_index(self, key):
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        index = self.hash_index(key)

        if self.table[index] is None:
            self.table[index] = HashTableEntry(key, value)
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = HashTableEntry(key, value)

        if self.get_load_factor() >= 0.7:
            self.resize(self.capacity * 2)
        return
        

    def delete(self, key):
        index = self.hash_index(key)
        current = self.table[index]

        if current is None:
            return
        elif current.key is key:
            if current.next is not None:
                self.table[index] = current.next
            else:
                self.table[index] = None
        else:
            while current is not None:
                next = current.next
                if next.key is key:
                    current.next = next.next
                    next = None
                    return
                current = next

        if self.get_load_factor() <= 0.2:
            self.resize(self.capacity // 2)
        return

    def get(self, key):
        index = self.hash_index(key)
        current = self.table[index]

        if current is None:
            return None

        while current is not None:
            if current.key is key:
                return current.value
            current = current.next
        return None

    def resize(self, new_capacity):
        old_table = self.table
        self.table = [None] * new_capacity

        for item in old_table:
            if item is None:
                continue
            else:
                current = item
                while current is not None:
                    next = current.next
                    self.put(current.key, current.value)
                    current = next
                

        


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
