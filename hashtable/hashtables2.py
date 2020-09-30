
##djb2



#fnv


#put
# def put (key):
    ##hash the key
    
    # our_hash = djb2(key)


##get
class Node :
    def __init__(self, value):
        self.value = value 
        self.next = None
        
class LinkedList:
    def __init__(self) :
        self.head = None      

    def find (self, val):
        cur_node = self.head
        
        while cur_node is not None:
            
            if val is cur_node.value:
                
                return cur_node.value
            else:
                cur_node = cur_node.next
                
        return None
           
    def add_to_tail(self, val) :
        if self.head is None:
            self.head = Node(val)  
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = Node(val)
            
            
            
            
##Load factor is num of elements / num of buckets


## if load factor is < 0.2 using unnecessary amounts of memory
ll = LinkedList()
n1 = Node(3)
ll.head = n1
ll.add_to_tail(4)
ll.add_to_tail(5)
ll.add_to_tail(6)
           