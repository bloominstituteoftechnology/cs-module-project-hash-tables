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

    def __init__(self, capacity):
        self.capacity = MIN_CAPACITY
        self.count = 0
        self.storage = [None] * capacity

    def get_num_slots(self):

        return self.capacity

    def get_load_factor(self):
        return self.count / self.capacity
    # Your code here

    def fnv1(self, key):

        hash = 14695981039346656037
        bytes_representation = key.encode()
        for byte_of_data in bytes_representation:
            hash = hash * 1099511628211
            hash = hash ^ byte_of_data

        return hash

    def djb2(self, key):

        hash = 5381
        for element in key:
            hash = (hash * 33) + ord(element)
        return hash

    def hash_index(self, key):

        return self.fnv1(key) % self.capacity

    def put(self, key, value):

        index = self.hash_index(key)

        if self.storage[index] == None:
            self.storage[index] = HashTableEntry(key, value)
        else:
            position = self.storage[index]
            while position != None:
                if position.key == key:
                    position.value = value
                    return
                if position.next == None:
                    position.next = HashTableEntry(key, value)
                    return
                position = position.next

    def delete(self, key):

        self.put(key, None)
        self.count -= 1

    def get(self, key):
        index = self.hash_index(key)

        position = self.storage[index]
        while position != None:
            if position.key == key:
                return position.value
            position = position.next

        return None

    def resize(self, new_capacity):

        old_storage = self.storage
        old_capacity = self.capacity

        self.storage = [None] * new_capacity
        self.capacity = new_capacity

        for index in range(old_capacity):
            position = old_storage[index]
            while position != None:
                self.put(position.key, position.value)
                position = position.next


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
