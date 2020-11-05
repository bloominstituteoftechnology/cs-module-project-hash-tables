class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        currStr = ""
        curr = self.head
        while curr != None:
            currStr += f'{str(curr.value)} ->'
            curr = curr.next
        return currStr

    # return node w/ value
    # runtime: O(n) where n = number nodes
    def find(self, value):
        curr = self.head
        while curr != None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    # deletes node w/ given value then return that node
    # runtime: O(n) where n = number of nodes
    def delete(self, value):
        cur = self.head

        # special case if we need to delete the head
        if cur.value == value:
            self.head = cur.next
            return cur

        prev = None
        cur = cur.next

        while cur != None:
            if cur.value == value:
                prev.next = cur.next
                cur.next = None
                return cur
            else:
                prev = cur
                cur = cur.next

        return None

    # insert node at head of list
    # runtime: O(1)
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    # overwrite node or insert node at head
    # runtime: O(n)
    def insert_at_head_or_overwrite(self, node):
        existingNode = self.find(node.value) # O(n)
        if existingNode != None:
            existingNode.value = node.value
            return False
        else:
            self.insert_at_head(node) # O(1)
            return True

    def add_to_tail(self, value):
        # 0. create new node from value
        new_node = Node(value, None)
        # 1. check if list is empty
        if not self.head:
            # if list is empty, set both head and tail to new node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node