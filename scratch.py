def my_hash(s):
    sb = s.encode()
    total = 0
    for b in sb:
        total += b
    return total%8
i = my_hash("parth")
hash_table = [None]*8
hash_table[i] = "8 months"
##hash parth
##retrieve value at that hash


def get_length_timeatlambda(e):
    curr_hash = my_hash(e)
    return hash_table[curr_hash]
length_parth = get_length_timeatlambda("parth")
print("Parth has worked at Lambda for " + length_parth)
employees = {}




class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ## given a string of just parentheses
        ## go through the string
        ## keep track if something is the correct closing parentheses
        ## O(N) where n is length of the string
        ## {[]}
        stack = []
        par_mapping = {"}" : "{", "]" : "[", ")" : "("}
        for p in s:
            if p in par_mapping:
                if len(stack) == 0:
                    return False
                most_recent = stack.pop()
                if par_mapping[p] != most_recent:
                    return False
            else:
                stack.append(p)
        if len(stack) != 0:
            return False
        return True


# LL
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def find(self, value):
      #start at the head
      #loop through the list
      #find value
      #return the node
      cur = self.head
      #while next is not none keep looping through
      while cur is not None:
          if cur.value == value:
              return cur
          cur = cur.next
      return None   


    def delete(self, value):
      cur = self.head
      # if head value is value
      if cur.value == value:
          # reassign head value to next
          self.head = cur.next
          return cur
          # reassigning pointers, not actually deleting the node itself
      prev = cur
      cur = cur.next
      while cur is not None:
          if cur.value == value:
            prev.next = cur.next
            return cur
          else:
              prev = cur
              cur = cur.next
            
      return None

      
    def insert_at_head(self, node):
        #first set next to current head
        node.next = self.head
        # set the node to new head
        self.head = node
      

cache={}
def fib(n):
    if <=1:
        return n
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)

    return cache[n]

# lists keep things in order
my_list = []
​
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
​
# why are dictionaries not in order? i.e., order is not guaranteed
## everything hashes differently
## don't know what index the hash function will return
​
my_list = [5, 3, 4, 2, 6, 7, 8, 1, 9]
​
d = {
    'Austin': 12,
    'Michael': 24,
    'Troy': 35,
    'Jorge': 99,
    'David': 42
}
​
# how can we sort our dictionary?
​
# turn into a list
for pair in d.items():
    print(pair)
​
# d.items().sort()
​
print(sorted(d.items()))
​
sorted_list_of_items = list(d.items())
sorted_list_of_items.sort()
​
print(sorted_list_of_items)
