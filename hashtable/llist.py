class Node:
    def __init__(self, value):
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

        return None  # we didn't find it
        

    def insert_at_head(self, value):
        n = Node(value)
        n.next = self.head
        self.head = n

#         head
#          v
# (55) -> (11) -> (22) -> (33) -> (44) -> None
#  c

def delete(self, value):
    cur = self.head

    # Special case of deleting the head

    if cur.value == value:  # Are we deleting the head?
        self.head = self.head.next
        cur.next = None
        return cur

    # General case

    prev = cur
    cur = cur.next

    while cur is not None:
        if cur.value == value:
            prev.next = cur.next  # cuts out the node
            cur.next = None
            return cur
        else:
            prev = prev.next
            cur = cur.next
    return None

    # def append(self, value):
    #     # TODO
    #     pass

ll = LinkedList()
# ll.insert(11)
# ll.insert(22)