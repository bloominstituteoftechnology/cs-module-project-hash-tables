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

    def __repr__(self):
        return f'Node({repr(self.value)})'

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        r = ""
        cur = self.head

        while cur is not None:
            r += f'({cur.value})'
            if cur.next is not None:
                r += ' -> '

            cur = cur.next

        return r

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

    def delete(self, value):
        cur = self.head

        # Special case of deleting the head of the list

        if cur.value == value:
            self.head = self.head.next
            return cur

        # General case

        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.value == value:  # Delete this one
                prev.next = cur.next   # Cuts out the old node
                return cur

            else:
                prev = prev.next
                cur = cur.next

        return None


if __name__ == "__main__":
    ll = LinkedList()

    print(ll)
    ll.insert_at_head(Node(11))
    print(ll)
    ll.insert_at_head(Node(22))
    print(ll)
    ll.insert_at_head(Node(33))
    print(ll)

    print(ll.find(22))
    print(ll.find(00))

    print(ll.delete(00))
    print(ll.delete(22))
    print(ll)

    print(ll.delete(33))
    print(ll)

    print(ll.delete(11))
    print(ll)
