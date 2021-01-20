class Node:
# this is a Constructor in
    def __init__(self, value): 
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f'Node({repr(self.value)})'
        # this is a way of printing out the node value out nicely

head = None

def insert_at_front(val):
    global head
    # Make a new node
    new_node = Node(val)
    
    # Point to new node next at head
    new_node.next = head

    # Point head to new node
    head = new_node

def print_list():
    # telling python to look at the global variable head since we do not have a variable head in local scope. Python since you don't set the scope of variables and everything you do in a function it treats as local so in cur = head it would throw out an error if we did not say hey python when you see head we are talking about the one in global scope
    global head
    # set cur(current) to head
    cur = head
    
    # Loop while cur.next is none
    while cur is not None:
        #Print value at cur
        print(cur.value, end =" ")
        # set cur to cur.next
        cur = cur.next
    print()

# deleting the head node
def delete_head():
    global head

    old_next = head.next
    head.next = None

    head = head.next

# what if we wanted to delete a node out of the middle
# walk through the list, find target get rid of target and join any remaining nodes together
def delete_node(value):
    global head
    # special case if list is empty
    if head is None:
        return
    # special case to delete head also
    if head.value == value:
        delete_head()
        return
# General case of deleting something in the middle
    prev = head
    cur = head.next

    while cur is not None:
        if cur.value == value:
            # print(f"Found it! {prev.value}, {cur.value}")
            prev.next = cur.next
            cur.next = None
            return
            
        cur = cur.next
        prev = prev.next

    # print("Didn't Find it")


    





insert_at_front(45)
insert_at_front(88)
insert_at_front(24)
insert_at_front(12)

print(head.value)
# should be 88
print(head.next.value)
# should be 45
print(head.next.next)
# should be none, null
# print(head.next.next.next.value)
# this would throw an error there is no third next and not value
# no we could go through the list this way but this takes up too much time it complicated instead we can create a loop to go through it. line 24*

print_list()

# delete_head()

print_list()

delete_node(88)

print_list()