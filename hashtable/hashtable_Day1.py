import math   # for power function

class HashTableEntry:
     """
     Linked List hash table key/value pair
     # could use Double LL but deleting/inserting from middle is rare with hash tables and managing prev, next overhead usually overkill
     """
     def __init__(self, key, value):
          # self.key = key
          # self.value = value
          # self.next = None
          self.key = key   # Day 1, index
          self.value = value # Day 1, element value
          self.next = None # Day 2, pointer to next node in LL
          self.last = None  # pointer to tail

     # def __str__(self):
     #      print(f' at key {self.key} >> value is: {str(self.value)}')

     # def __repr__(self):
     #      print(f' Entry({repr(self.value)})')     

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
     """
     A hash table that with `capacity` buckets
     that accepts string keys

     Implement this.
     """
 
     def __init__(self, capacity):
          #self.capacity = MIN_CAPACITY  # Day 1, size here is same a number of slots, until we deal with collisions
          #self.slots = [ None for item in range(self.capacity)]
          # Day 2
          self.capacity = capacity
          self.slots = [None] * capacity  # this hold LL (e.g. HashTableEntry)
          self.items_stored = 0           # inc/dec for items added/deleted
          

     def get_num_slots(self):
          """
          Return the length of the list you're using to hold the hash
          table data. (Not the number of items stored in the hash table,
          but the number of slots in the main list.)

          One of the tests relies on this.

          Implement this.
          """
          # Your code here
          return len(self.slots)

     def get_load_factor(self):
          """
          Return the load factor for this hash table.
               load Factor = (# of items stored) / (total # of slots)
               Good practice is to resize when load factor > 0.7
               CANNOT COPY OLD ITEMS into resized hashtable, new size means modulus is different, hence new hashes & new indices
               'Amortized' complexity is O(1)
          Implement this.
          """
          # Your code here


          load_factor = round( (( self.items_stored)/(self.get_num_slots())), 1)
          # load_factor = round( (( self.items_stored)/(self.capacity), 1)
          # # calc_num_slots = get_num_slots()

          print(f' Current load factor {load_factor}')
          
          return load_factor

     def find_scale_factor(self):
          orig_load_factor = self.get_load_factor()

          if orig_load_factor > 0.7:
               scale_calc = 2
          elif orig_load_factor < 0.2:
               scale_calc = 0.5
          else:
               return
      
          self.resize(int(scale_calc * self.capacity))
          # return scale_calc
          

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
               #salt = 5381
          hash_val = 5381     

          for ch in key:
               hash_val = ((hash_val << 5) + hash_val) + ord(ch)
               # hash_val = (hash_val * 33) + ord(ch)     

          # print(f' \n dbj2 with key {key} gives hash_val >> {hash_val} ')
          # return hash_val & 0xFFFFFFFF
          return hash_val   

     def hash_index(self, key):
          """
          Take an arbitrary key and return a valid integer index
          between within the storage capacity of the hash table.
          """
          #return self.fnv1(key) % self.capacity
          # print(f' \t %%%  key {key} gives djb2 hash of {self.djb2(key)}')
          return self.djb2(key) % self.capacity

     def put(self, key, value):
          """
          Store the value with the given key.

          Hash collisions should be handled with Linked List Chaining.
          # we make an array of linked list nodes
          Implement this.
          """
          # Your code here
          # Day 1
          # hashed_index = self.hash_index(key)

          # if self.slots[hashed_index] != None:
          #      print(f' \n\t Collision at key {key} with hashed_index {hashed_index} & overwrite of {self.slots[hashed_index]}')

          # self.slots[hashed_index] = value
          # print(f' put: using key {key } >> index {hashed_index} >>> value is    \"{self.slots[hashed_index]}\"')

          # Day 2  - add to tail method
          hashed_index = self.hash_index(key)

          # # create new node
          # new_tail = HashTableEntry(key, value)   
          # current =  self.slots[hashed_index]      

          # WATCH THIS COUNT for overwrites to same key

          # test if slot NOT empty
          if self.slots[hashed_index] != None:
               print(f' \n\t Collision at key {key} with hashed_index {hashed_index} & value {self.slots[hashed_index].value}')


               # create new node
               new_tail = HashTableEntry(key, value)   
               current =  self.slots[hashed_index]      

               print(f' BEFORE  Current key is {current.key} with value {current.value} ')
               if current.key == key:
                    # print(f' overwrite at HEAD, value changed to {value}')
                    current.value = value
                    return

               # iterate to find tail & check for same key overwrite 
               while current.next != None:
                    current = current.next
                    if current.key == key:
                         current.value = value
                         # print(f' AFTER HEAD , overwrite value changed to {value}')
                         return

               # append to tail
               current.next = new_tail  

          # slot empty, add first HashTableEntry       
          else:  
               # print(f' \n\t Create HashItem at key {key} with hashed_index {hashed_index} value: {value}')    
               self.slots[hashed_index] = HashTableEntry(key, value)
          
          # Increment ONLY for new items added
          self.items_stored += 1
          # self.find_scale_factor()

          # Idea is to try to append to tail in O(1) if I have a tail pointer
          self.last = self.slots[hashed_index]
          print(f' current tail on index {hashed_index} is {self.last.value} ')
          if self.get_load_factor() > 0.7:
               self.find_scale_factor
          elif self.get_load_factor() < 0.2:
               self.find_scale_factor
          else:
               return          

     def delete(self, key):
          """
          Remove the value stored with the given key.

          Print a warning if the key is not found.

          Implement this.
          """
          # Your code here
          # Day 1
          # if key in range(self.capacity):
          #      self.slots[key] = None
          # else:
          #      print(f' Cannot delete key that does not exist ')     
          # hashed_index = self.hash_index(key)
          # print(f' delete:  key {key}, hashed_index{hashed_index}')
          # self.slots[hashed_index] = None

          # Day 2
          hashed_index = self.hash_index(key)
          current = self.slots[hashed_index]

          # Easy case, key not found if no insertions made
          if current == None:
               print(f'key not found')
               return
          else:
          # key is at head with no chaining
               if current.key == key:
                    current.value = None
                    print(f' key {current.key} value changed to {current.value}')      
               else: 
                    current = current.next
                    # iterate and look for key, set value to None if found
                    while current != None:
                         if current.key == key:
                              current.value = None
                         # goto next entry
                         current = current.next     
                         
                         # checks last item in chain
                         if current == None:
                              print(f' KEY NOT FOUND in chain ')     
                              return
           # Decrement items deleted
          self.items_stored -= 1
          # self.find_scale_factor()

     def get(self, key):
          """
          Retrieve the value stored with the given key.

          Returns None if the key is not found.

          Implement this.
          """
          # Your code here
          # Day 1 
          # hashed_index = self.hash_index(key)
          # value = self.slots[hashed_index]
          # print(f' get: key {key} value at index {hashed_index} is {value}')
          # return self.slots[hashed_index]

          # Day 2
          # Find hashed index and iterate until key located, return val OR None if not found
          hashed_index = self.hash_index(key)

          if self.slots[hashed_index] == None:
               return None
          else:
              ## Look for key !
               if self.slots[hashed_index].key == key:
                   return self.slots[hashed_index].value
               else:  # check next item
                    current = self.slots[hashed_index].next
                    while current != None: # Loop until end of entries     
                         if current.key == key: # check for key
                              return current.value
                         else:
                              current = current.next

               # if current is None:
               #      return None          

     def resize(self, new_capacity):
          """
          Changes the capacity of the hash table and
          rehashes all key/value pairs.
               ?? Resize down when load factor <= 0.7
          Implement this.
          """
          # Your code here
          change_size = HashTable(new_capacity)
          for slot in self.slots:
               if slot != None:
                    slot_item = slot
                    while slot_item != None:
                         print(f' slot_item is {slot_item}')
                         change_size.put(slot_item.key, slot_item.value)
                         # increment though chain
                         slot_item = slot_item.next

          self.capacity = change_size.capacity
          self.slots = change_size.slots
          

          print(f' items_stored  {self.items_stored}')
          print(f' # slots {len(self.slots)}')
          if new_capacity == len(self.slots):
               print(f' RESIZE SUCCESS !!')


if __name__ == "__main__":
     ht = HashTable(128)

     print(f' # slots func: {ht.get_num_slots()}')
     # print(ht.get_num_slots())
     # # print("****** OVERLOADING TABLE ******")

     # print(ht.delete("line_1"))     
     # print(ht.slots)

     # ht.put("line_1", "'Twas brillig, and the slithy toves")
     # ht.put("line_2", "Did gyre and gimble in the wabe:")


     # print(ht.delete("line_1"))


     # print(ht.delete("WEIRD KEY"))
 

     ht.put("line_2", "Did gyre and gimble in the wabe:")
     ht.put("line_3", "All mimsy were the borogoves,")
     # ht.put("line_4", "And the mome raths outgrabe.")
     # ht.put("line_5", '"Beware the Jabberwock, my son!')
     # ht.put("line_6", "The jaws that bite, the claws that catch!")
     # ht.put("line_7", "Beware the Jubjub bird, and shun")
     # ht.put("line_8", 'The frumious Bandersnatch!"')
     # ht.put("line_9", "He took his vorpal sword in hand;")
     # ht.put("line_10", "Long time the manxome foe he sought--")
     # ht.put("line_11", "So rested he by the Tumtum tree")
     # ht.put("line_12", "And stood awhile in thought.")

     # print(f" \t **** GET test")
     # print(ht.get("line_1"))
     # print(ht.get("line_2"))
     # print(ht.get("line_3"))
     # print(ht.get("line_4"))
     # print(ht.get("line_5"))
     # print(ht.get("line_6"))
     # print(ht.get("line_7"))
     # print(ht.get("line_8"))
     # print(ht.get("line_9"))
     # print(ht.get("line_10"))
     # print(ht.get("line_11"))
     # print(ht.get("line_12"))

     # # # # print out our HT
     # # # for ind in range(8):
     # # #      slot_num = ht.slots[ind]
     # # #      print(f' slot_num: {ind} key: {slot_num.key} value: {slot_num.value}' )

     # # print(f" total items stored {ht.items_stored}")
     # # print(f" \t **** GET test")

     # # # print(ht.get("line_1"))
     # # # print(ht.get("line_2"))
     
     # print(f" \t **** REWRITE TEST")
     # ht.put("line_1", "'OOOOOOO Twas brillig, and the slithy toves")
     # ht.put("line_2", "OOOOOOOO Did gyre and gimble in the wabe:")
     # ht.put("line_3", "OOOOOOOOAll mimsy were the borogoves,")
     # ht.put("line_4", "OOOOOOOOAnd the mome raths outgrabe.")
     # ht.put("line_5", '"OOOOOOOOBeware the Jabberwock, my son!')
     # ht.put("line_6", "OOOOOOOOThe jaws that bite, the claws that catch!")
     # ht.put("line_7", "OOOOOOOOBeware the Jubjub bird, and shun")
     # ht.put("line_8", 'OOOOOOOOThe frumious Bandersnatch!"')
     # ht.put("line_9", "OOOOOOOOHe took his vorpal sword in hand;")
     # ht.put("line_10", "OOOOOOOOLong time the manxome foe he sought--")
     # ht.put("line_11", "OOOOOOOOSo rested he by the Tumtum tree")
     # ht.put("line_12", "OOOOOOOOAnd stood awhile in thought.")

     # print("")

     # print(f" \t **** OVERWRITE test")
     # print(ht.get("line_1"))
     # print(ht.get("line_2"))
     # print(ht.get("line_3"))
     # print(ht.get("line_4"))
     # print(ht.get("line_5"))
     # print(ht.get("line_6"))
     # print(ht.get("line_7"))
     # print(ht.get("line_8"))
     # print(ht.get("line_9"))
     # print(ht.get("line_10"))
     # print(ht.get("line_11"))
     # print(ht.get("line_12"))
     
     print(ht.get_num_slots())
     
     print(ht.get_load_factor())

     print(ht.find_scale_factor())
     print(ht.capacity)

     # ht.resize(16)
     # print(ht.get_load_factor())

     # ht.resize(4)
     # print(ht.get_load_factor())

     # print(f" total items stored {ht.items_stored}")
     # print(f" \t **** DELETE test ")
     # ht.delete("line_1")
     # ht.get("line_1")

     # print(f' $$$$$    Show entire table $$$$$$$$ \n')
     # print(f' all slots {ht.slots}')
     # print(ht.slots)
     # # Test storing beyond capacity
     # for i in range(1, 13):
     #      print(ht.get(f"line_{i}"))

     # # Test resizing
     # old_capacity = ht.get_num_slots()
     # ht.resize(ht.capacity * 2)
     # new_capacity = ht.get_num_slots()

     # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

     # # Test if data intact after resizing
     # for i in range(1, 13):
     #      print(ht.get(f"line_{i}"))

     # print("")

## First pass
# print(f' ht capacity  is >> {ht.capacity} ')
# print(ht.slots)
# print(ht.get(1))
# print(ht.get(100))

# print(ht.put(2, "Apple"))
# print(ht.put(3, "Orange"))
# print(ht.slots)

# print(ht.put(200, "Apple"))
# print(ht.slots)

# print(ht.delete(2))
# print(ht.slots)

# print(ht.delete(100))

# print(ht.hash_index("Value"))
# print("")
# print(ht.hash_index("line_1"))
# print(ht.hash_index("LLLine_1"))

# print(f'{177622 % 8}')
# print(f'{5381 << 5}')