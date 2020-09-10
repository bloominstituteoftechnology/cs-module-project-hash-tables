

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
    def delete(self,value):
        curr = self.head

        if curr.value == value:
            self.head = curr.next
            return curr

        prev = curr
        curr = curr.next

        while curr is not None:
            if curr.value == value:
                prev.next == curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next

        return None



#   Runtime 0(number of nodes)
    def find(self, value):
        curr = self.head

        while curr is not  None:
            if curr.value == value:
                return cur
            curr = curr.next

        return None

a = Node(1)
b = Node(2)
c = Node(3)


ll = LinkedList()
ll.insert_at_head(a)
ll.insert_at_head(b)
ll.insert_at_head(c)
print(ll)

print(ll.find(5))

ll.delete(3)
print(ll)