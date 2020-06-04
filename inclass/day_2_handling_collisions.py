"""
head
 v
(W) -> (X) -> (Z) -> (99) -> (A) -> (B) -> (C) -> None
 ^
cur
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
    
    def find(self, value):
        cur = self.head   # cur and head start as same, but cur walks down the list

        while cur is not None:
            if cur.value = value:
                # found it!
                return cur

            cur = cur.next
        
        return None


    def delete(self, value):
        """
        head
        v
        (W) -> (X) -> (Z) -> (99) -> (A) -> (B) -> (C) -> None
        ^       ^
        prev    cur
        """

        cur = self.head

        # Special case of deleting the head of the list
        if cur.value == value:
            self.head = self.head.next
            return cur

        # General case
        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.value == value: # Delete this one
                prev.next = cur.next # cuts out the old node,.
                return cur
            else:
                prev = prev.next
                cur = cur.next

        # If the value is not in the list        
        return None


if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_head(Node(11))