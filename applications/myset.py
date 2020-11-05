# Partial implementation of a set using a hashtable​

class Set:
    def __init__(self):
        self.data = {}​

    def add(self, value):
        self.data[value] = True​

    def in_set(self, value):
        return value in self.data​

s = Set()
s.add(1)
s.add(2)
s.add(3)​

print(s.in_set(2))
print(s.in_set(22))