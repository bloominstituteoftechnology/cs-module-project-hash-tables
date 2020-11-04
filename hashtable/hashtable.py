class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        if isinstance(other, HashTableEntry):
            return self.key == other.key
        return False


class LinkedList:
  def __init__(self):
    self.head = None

  def __repr__(self):
    currStr = ""
    curr = self.head
    while curr != None:
      currStr += f"{str(curr.value)} ->"
      curr = curr.next
    return currStr

  def find(self, value):
    # return node with value
    curr = self.head

    #walk through the LL and check the value
    while curr != None:
      if curr.value == value:
        return curr
      curr = curr.next

    return None

  def delete(self, value):
    curr = self.head

    # special case for remove head
    if curr.value == value:
      self.head = curr.next
      curr.next = None
      return curr

    prev = None

    while curr != None:
      if curr.value == value:
        prev.next = curr.next
        curr.next = None
        return curr
      else:
        prev = curr
        curr = curr.next

    return None

  # insert node at head of list
  def add_to_head(self, node):
    node.next = self.head
    self.head = node

  # overwrite node or insert node at head
  def insert_at_head_or_overwrite(self, node):
    existing_node = self.find(node.value)
    if existing_node != None:
      existing_node.value = node.value
      return False
    else:
      self.add_to_head(node)
      return True

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.count = 0


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
        return self.count / self.get_num_slots()


    def fnv1(self, key):
        pass


    def djb2(self, key):
        hash = 5381
        for s in key:
            hash = ((hash << 5) + hash) + ord(s)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        # hash the key and get the index
        index = self.hash_index(key)
        # check if the table at index is empty
        if self.table[index] == None:
            # if it is -> initialize new LinkedList
            ll = LinkedList()
            ll.add_to_head(Node(HashTableEntry(key, value)))
            self.table[index] = ll
            # increase count
            self.count += 1
        else:
            # if table at index already has a LL, get reference to current LL
            curr_ll: LinkedList = self.table[index]
            # set the new Node as the head
            did_add_new_node = curr_ll.insert_at_head_or_overwrite(Node(HashTableEntry(key, value)))
            if did_add_new_node:
            # increase count
                self.count += 1

        if self.get_load_factor() > 0.7:
            self.resize(self.get_num_slots() * 2)

        


    def delete(self, key):
        index = self.hash_index(key)
        if self.table[index] != None:
            ll: LinkedList = self.table[index]
            did_delete_node = ll.delete(HashTableEntry(key, None))
            if did_delete_node != None:
                self.count -= 1
                if self.get_load_factor() < 0.2:
                    self.resize(self.get_num_slots() / 2)
        else:
            print("Warning Node not found")


    def get(self, key):
        index = self.hash_index(key)
        if self.table[index] != None:
            ll: LinkedList = self.table[index]
            node = ll.find(HashTableEntry(key, None))
            if node != None:
                return node.value.value
        return None



    def resize(self, new_capacity):
        old_table = self.table
        self.table = [None] * int(new_capacity)
        self.count = 0
        self.capacity = new_capacity

        for element in old_table:
            if element == None:
                continue
            curr_node: Node = element.head
            while curr_node != None:
                temp = curr_node.next
                curr_node.next = None
                index = self.hash_index(curr_node.value.key)

                if self.table[index] != None:
                    self.table[index].add_to_head(curr_node)
                else:
                    ll = LinkedList()
                    ll.add_to_head(curr_node)
                    self.table[index] = ll

                curr_node = temp
                self.count += 1

    def check_and_resize(self):
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)
        elif self.get_load_factor() < 0.2:
            self.resize(self.capacity / 2)



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

    ht.delete("line_1")

    print("deleted")
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
