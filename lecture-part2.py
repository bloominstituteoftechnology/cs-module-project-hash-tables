

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
        while cur is not None:
            curStr += f'{str(curr.value)} -> '
            cur = cur.next
        return curStr

    # def insert_at_head(self, node):

    #  def delete 

    def find(self, value):
        cur = self.head

        while cur is not  None:
            if cur.value == value:
                return cur
            cur = cur.next

        return None
