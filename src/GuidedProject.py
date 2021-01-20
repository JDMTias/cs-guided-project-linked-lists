class Node:
    # this is a Constructor in
    def __init__(self, value): 
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f'Node({repr(self.value)})'
    

head = Node(45)
o = Node(88)
# head.next does not make a copy it makes a new reference, this is how we link node n and node 0
head.next = o

p = Node(2)

print(head.value)
print(head.next)