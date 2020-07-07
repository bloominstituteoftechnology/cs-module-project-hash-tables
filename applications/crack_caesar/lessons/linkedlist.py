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

        cur = cur.next

        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next
        
        return None

    def delete(self, value):
        cur = self.head

        if cur.value == value:
            self.head = cur.next
            return cur


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
        node.next = self.head
        self.head = node


