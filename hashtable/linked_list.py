
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None

    def add_to_head(self, key, value):
        new_node = HashTableEntry(key, value)
        if self.head == None:
            self.head = new_node
            # self.tail = new_node
            self.next = None
        else:
            oldhead = self.head
            self.head = new_node
            self.head.next = oldhead

    def find(self, key):
        current = self.head
        while current != None:
            if current.key == key:
                return current.value
            else:
                current = current.next
        return None

    def delete(self, key):
        current = self.head

        if current.key == key:
            self.head = current.next
            return current.value

        prev = current
        current = current.next

        while current != None:
            if current.key == key:
                prev.next = current.next
                return current.value
            else:
                prev = current
                current = current.next
        return None


dude = LinkedList()
dude.add_to_head("hello", "mate")
dude.delete("hello")
print(dude.find("hello"))
# this should work
