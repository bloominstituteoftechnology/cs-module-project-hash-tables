class LinkedList:
    def __init__(self):
        self.head = None
        
    def __repr__(self):
        return f"{self.head.value}"

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def find(self, value):
        cur_node = self.head

        while cur_node is not None:
            if cur_node.value == value:
                return cur_node
            cur_node = cur_node.next
        return None

    def delete(self, value):

        curr_node = self.head

        if(curr_node == None):
            return None

        if(curr_node.value == value):
            old_head = self.head
            
            self.head = self.head.next
            old_head.next = None
            return old_head

        prev = self.head

        while(curr_node is not None):
            if(curr_node.value == value):
                prev.next = curr_node.next
                curr_node = None
                return curr_node
            prev = prev.next
            curr_node = curr_node.next

        return None
    
    def __str__(self):
        r = ""

        curr_node = self.head

        while curr_node is not None:
            r += f"{curr_node.value}"
            
            if curr_node.next is not None:
                r += " -> "

            curr_node = curr_node.next