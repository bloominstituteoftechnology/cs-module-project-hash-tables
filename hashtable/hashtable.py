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
        # Your code here
        self.buckets = [LinkedList()] * capacity
        self.capacity = capacity
        
        

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
        # Your code here
        hash = 5381

        for char in key:
            hash = ((hash << 5) + hash) + ord(char)

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
        # Your code here
        h = self.djb2(key)
        i = self.hash_index(key)
        
        # create a new node from the key value pair
        new_node = Node(key, value)

        #check to see if a node exists in the spot where we want to place this node
        existing_node = self.buckets[i].head

        if existing_node:
            last_node = None
            while existing_node:
                if existing_node.key == key:
                    existing_node.value = value
                    return 
                last_node =  existing_node
                existing_node = existing_node.next

            last_node.next = new_node

        else:
            self.buckets[i].append(new_node)

        return self.buckets[i].head    
         

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        h = self.djb2(key)
        i = self.hash_index(key)

        #check to see if the entry exists
        e = self.buckets[i].head
        #check to see if exists is not None.
        while e:
            #If we find a match, then remove it.
            if e.key == key:
                if last:
                    last.next = e.next
                else:
                    self.buckets[i].remove(e.next)    
            #swap removed item so a newer item is stored.
            last = e
            e = e.next        
            

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        h = self.djb2(key)
        i = self.hash_index(key)
        
        # check the head node 
        look_up = self.buckets[i].head
        # if the head exists
        if look_up is not None:
            # while there is still something in the array
            while look_up is not None:
            #found 
                if look_up.key == key:
                    return look_up.value  

                look_up = look_up.next      
            
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur

            cur = cur.next                

        return None
     #add to tail
    def append(self, value): 
        n = Node(value, value)  

        #no head
        if self.head is None:
            self.head = n  

        else:
            cur = self.head

            while cur.next is not None:
                cur = cur.next

            cur.next = n       

    def remove(self, value):
        cur = self.head

        # empty list 
        if cur is None:
            return None

        # remove head
        if cur.value == value:
            self.head = cur.next
            return cur

        else:
            prev = cur
            cur = cur.next
            while cur is not None:
                if cur.value == value:
                    prev.next = cur.next
                    return cur
                else:
                    prev = cur
                    cur = cur.next                     

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
