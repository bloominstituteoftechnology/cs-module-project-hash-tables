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
      currStr += f"{str(curr.value)} ->"
      curr = curr.next
    return currStr

  def find(self, value):
    # return node with value
    curr = self.head

    #walk through the LL and check the value
    while curr != None:
      if curr.value == value:
        return curr
      curr = curr.next

    return None

  def delete(self, value):
    curr = self.head

    # special case for remove head
    if curr.value == value:
      self.head = curr.next
      curr.next = None
      return curr

    prev = None

    while curr != None:
      if curr.value == value:
        prev.next = curr.next
        curr.next = None
        return curr
      else:
        prev = curr
        curr = curr.next

    return None

  # insert node at head of list
  def add_to_head(self, node):
    node.next = self.head
    self.head = node

  # overwrite node or insert node at head
  def insert_at_head_or_overwrite(self, node):
    existing_node = self.find(node.value)
    if existing_node != None:
      existing_node.value = node.value
    else:
      self.add_to_head(node)


a = Node(1)
b = Node(2)
c = Node(3)

ll = LinkedList()

ll.add_to_head(c)
ll.add_to_head(b)
ll.add_to_head(a)
ll.insert_at_head_or_overwrite(c)
ll.delete(2)

print(ll)