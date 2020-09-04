

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def __repr__(self):
        curStr = ""
        curr = self.head
        while curr is not None:
            curStr += f'{str(curr.value)} -> '
            curr = curr.next
        return curStr

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
    

    #  def delete 

#   Runtime 0(number of nodes)
    def find(self, value):
        curr = self.head

        while curr is not  None:
            if curr.value == value:
                return cur
            curr = curr.next

        return None
