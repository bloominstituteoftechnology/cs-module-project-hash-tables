class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, value):
        #start at the head
        curr = self.head
        #loop through the list
        while curr is not None:
            #find value
            if curr.value==value:
                 #return the node
                return curr
            curr = curr.next
        return None

    def delete(self, value):
        curr = self.head

        # if the value is the head
        if curr.value == value:
            self.head = curr.next
            return curr
        
        # reassign pointers
        prev = curr
        curr = curr.next
        
        while curr is not None:
            if curr.value==value:
                # readdress the pointers
                prev.next == curr.next
                return curr
            else:
                prev = curr
                curr = curr.next
        
        return None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node