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

    def __repr__(self):
        return f'HashTableEntry({self.key},{self.value}'

# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
    
#     def __repr__(self):
#         return f'Node({self.value})'

    
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self): # Walking through Linked list and printing it out whats within it. 
        currStr = ""
        curr = self.head
        while curr != None:
            currStr += f'{str(curr)}'
            curr = curr.next
            return currStr
        #Helper Methods
        #O(n) where n is number of nodes 
    def find(self, value):
        cur = self.head
        
        while cur is not None:
            if cur == value:
                return cur

            cur = cur.next

        return None
        #O(n) where n is number of nodes 
    def delete(self,value):
            # deletes node with given value
        curr = self.head

            #Special case if we want to delete the head
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
        #O(1) where n is number of nodes             
    def insert_at_head(self,node):
        node.next = self.head
        self.head = node
        #O(n) where n is number of nodes  because of 'find'
    def insert_at_head_or_overwrite(self,node):
            #insert node at head or overwrite the node
        existing_node = self.find(node.value)
        if existing_node != None:
            existing_node.value = node.value
            return False
        else:
            self.insert_at_head(node)
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
        
        self.table = [None] * capacity
        self.capacity = capacity
        self.num_elements = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.table) #self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Load factor = num of elements in hash table/ num of slots 
        return self.num_elements/self.get_num_slots()


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):  #http://pythontutor.com/visualize.html#mode=display 
        hash = 5381
        for x in key:
        # ord(x) simply returns the unicode rep of the
        # character x
            hash = (( hash << 5) + hash) + ord(x)
            # Note to clamp the value so that the hash is 
            # related to the power of 2
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
       # self.table[self.hash_index(key)] = value --> Array implementation
        hash_index = self.hash_index(key)
        if self.table[hash_index] != None:
            linked_list = self.table[hash_index]
            did_add_new_node = linked_list.insert_at_head_or_overwrite(HashTableEntry(key,value))
            
            if did_add_new_node:
                self.num_elements +=1 
            
        else:
            linked_list = LinkedList()
            linked_list.insert_at_head(HashTableEntry(key,value))
            
            self.table[hash_index] = linked_list
            self.num_elements +=1

        if self.get_load_factor() > 0.7:
            self.resize(self.get_num_slots()*2)
        
        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # val = self.table[self.hash_index(key)] --> Array implementation 
        # if val == None:
        #     print('Value is already None')
        # self.table[self.hash_index(key)] = None
        hash_index = self.hash_index(key)
        if self.table[hash_index] != None:
            linked_list = self.table[hash_index]
            did_delete_node = linked_list.delete(HashTableEntry(key,None))
            if did_delete_node != None:
                self.num_elements -= 1
            if self.get_load_factor() < 0.2:
                print(f'load factor is {self.get_load_factor()}')
                print(f'self.get_num_slots()/2 is {self.get_num_slots()/2}')
                self.resize(self.get_num_slots()/2)

        else:
            print(f'This key does not exist!')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hash_index = self.hash_index(key)
        if self.table[hash_index] != None:
            linked_list = self.table[hash_index]
            
            node = linked_list.find(HashTableEntry(key,None))
            if node != None:
                return node.value
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_table = self.table
        self.table = [None]* int(new_capacity)
        self.num_elements = 0

        for element in old_table:
            if element is None:
                continue
            curr_node = element.head
            
            while curr_node != None:
                temp = curr_node.next 
                curr_node.next = None # remove the reference since its moving to new table 
                print(curr_node.key)
                hash_index = self.hash_index(curr_node.value.key) # this is where its going to be in new table 
                print (hash_index)

                if self.table[hash_index] != None:
                    self.table[hash_index].insert_at_head(curr_node) # Inseert at head if a linked list already exists in this new table
                else:
                    linked_list = LinkedList() # if nothing is present at this index, create new node and add it at head. 
                    linked_list.insert_at_head(curr_node)
                    self.table[hash_index] = linked_list

                curr_node = temp
                self.num_elements += 1 

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
