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
​
		# Special case of empty list
​
		if self.head is None:
			return None
​
		# Special case of deleting the head of the list
​
		if self.head.value == value:
			old_head = self.head
			self.head = self.head.next
			old_head.next = None
			return old_head
​
		# General case
​
		prev = self.head
		cur = self.head.next
​
		while cur is not None:
			if cur.value == value:
				prev.next = cur.next
				cur.next = None
				return cur
​
			prev = prev.next
			cur = cur.next
​
		# If we get here, we didn't find it
		return None

    
    def __str__(self):
        r = ""

        curr_node = self.head

        while curr_node is not None:
            r += f"{curr_node.value}"
            
            if curr_node.next is not None:
                r += " -> "

            curr_node = curr_node.next