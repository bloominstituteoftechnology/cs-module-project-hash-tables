# Load Factor

**load factor** = number of elements stored in hash table / number of slots

4 / 8 = 0.5
8 / 8 = 1.0
16 / 8 = 2.0

**How to know when to re-size?**

- If `load factor > 0.7`, grow the table
- If `load factor < 0.2`, shrink the table (down to some minimum)

Grow the table -> double in size
Shrink the table -> halve in size

```py
# When you PUT:
#     if `load_factor` > 0.7:
#         create new arr with double the size of old one
#         for each elem in old arr:
#             PUT in the new arr
```

---

# Beej Notes

## Collision Resolution Chaining
```sh
Collision resolution by chaining
--------------------------------
Make our array of slots into an array of linked lists.
Each linked list node is a HashTableEntry.
Put
---
Slot
Index Chain (linked list)
----- -------------------------------
 0    -> None
 1    {foo:12} -> None
 2    {baz:999} -> {bar:50} -> None
 3    -> None
put("foo", 12)   # hashes to 1
put("bar", 30)   # hashes to 2
put("baz", 999)  # hashes to 2 -- collision
put("bar", 50)   # hashes to 2 -- collision
1. Figure out the index
2. Search the linked list to see if the key is there
2a. If the key is there, overwrite the value
2b. If not there, create a new HashTableEntry and insert it in the list
Get
---
1. Figure out the index for the key
2. Search the linked list at the index for the HashTableEntry that matches the key
3. Return the value for the entry, or None if not found
Delete
------
1. Figure out the index for the key
2. Search the linked list at the index for the HashTableEntry that matches the key
2a. If found, delete the entry from the linked list--return the value
2b. If not found, return None
```

## LinkedList and Node
```sh
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
​
    def __repr__(self):
        return f'Node({repr(self.value)})'
​
class LinkedList:
    def __init__(self):
        self.head = None
​
    def __str__(self):
        """Print entire linked list."""
​
        if self.head is None:
            return "[Empty List]"
​
        cur = self.head
        s = ""
​
        while cur != None:
            s += f'({cur.value})'
​
            if cur.next is not None:
                s += '-->'
​
            cur = cur.next
​
        return s
​
    def find(self, value):
        cur = self.head
​
        while cur is not None:
            if cur.value == value:
                return cur
​
            cur = cur.next
​
        return None
​
    def delete(self, value):
        cur = self.head
​
        # Special case of deleting head
​
        if cur.value == value:
            self.head = cur.next
            return cur
​
        # General case of deleting internal node
​
        prev = cur
        cur = cur.next
​
        while cur is not None:
            if cur.value == value:  # Found it!
                prev.next = cur.next   # Cut it out
                return cur  # Return deleted node
            else:
                prev = cur
                cur = cur.next
​
        return None  # If we got here, nothing found
​
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
​
    def insert_or_overwrite_value(self, value):
        node = self.find(value)
​
        if node is None:
            # Make a new node
            self.insert_at_head(Node(value))
​
        else:
            # Overwrite old value
            node.value = value
​
if __name__ == "__main__":
    l = LinkedList()
    print(l)
    for i in range(5):
        l.insert_at_head(Node(i))
    print(l)
    print(l.delete(2))
    print(l)
    print(l.delete(4))
    print(l)
    print(l.delete(0))
    print(l)
​
    print(l.find(0))
    print(l.find(3))
    print(l.find(1))
​
    l.insert_or_overwrite_value(4)
    print(l)
    l.insert_or_overwrite_value(4)
    print(l)