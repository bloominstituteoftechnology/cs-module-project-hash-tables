class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return f'{self.value}'

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self,value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next
        return None # we did not find anything

    def insert_at_head(self,value):
         n = Node(value)
         n.next = self.head
         self.head = n

    def append(self, value):
        pass

    def delete(self,value):
        cur = self.head
        #special case deleting the head
        if cur.value == value:
            self.head = self.head.next
            cur.next = None
            return cur

        #general case
        prev = cur
        cur = cur.next
        while cur is not None:
            if cur.value == value:
                prev.next = cur.next
                cur.next = None
                return cur
            else:
                prev = prev.next
                cur = cur.next
        return None

ll = LinkedList()
ll.insert_at_head(11)
ll.insert_at_head(22)

print(ll.head)
# Load factor
'''
The number of records in the hash table vs. the number of slots in the array

data = [None] * 16

put('1', 99)
put('2', 99)
put('3', 99)
put('4', 99)
put('5', 99)
put('6', 99)
put('7', 99)
put('8', 99)
put('9', 99)
put('10', 99)

load factor = 10/16

if the load is 1.0, we exactly the name number of data elements as array elements.
'''