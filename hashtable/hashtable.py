class Node:
  def __init__(self, value, key):
    self.value = value
    self.key = key
    self.next = None

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

  def delete(self, key):
    curr = self.head

    # special case for remove head
    if curr.key == key:
      self.head = curr.next
      curr.next = None
      return curr

    prev = None

    while curr != None:
      if curr.key == key:
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
    else:
      self.add_to_head(node)

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
            # set table at index to newly created LL
            self.table[index] = ll
            # add created node to the head of the LL
            ll.add_to_head(Node(value, key))
            # increase count
            self.count += 1
            self.check_and_resize()
        else:
            # if table at index already has a LL, get reference to current LL
            curr_ll: LinkedList = self.table[index]
            # set the new Node as the head
            curr_ll.add_to_head(Node(value, key))
            # increase count
            self.count += 1
            self.check_and_resize()

        


    def delete(self, key):

        # value = self.table[self.hash_index(key)]
        # if value == None:
        #     print("No value for index")
        # self.table[self.hash_index(key)] = None
        index = self.hash_index(key)
        ll: LinkedList = self.table[index]
        ll.delete(key)
        self.check_and_resize()


    def get(self, key):

        return self.table[self.hash_index(key)]


    def resize(self, new_capacity):
        old_table = self.table
        self.table = [None] * new_capacity

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
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")
