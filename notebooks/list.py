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
        cur = self.head

        # walk the linked list
        while cur is not None:
            if cur.value == value:
                # Found it!
                return cur

            cur = cur.next

        return None


"""
head
   v
  (W) --> (X) --> (Z) --> (99) --> (A) --> (B) --> (C) --> None
                ^            ^
                prev     cur
"""


if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_head(Node(11))
