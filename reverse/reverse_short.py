class Node:
    def __init__(self, value):
        self.value = value
        self.next_1 = None


# make a short linked list
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.next_1 = node2
node2.next_1 = node3
node3.next_1 = node4
node4.next_1 = node5
node5.next_1 = None


def reverse_parent_function(node):
    # step 1: run recursive reverse_order function
    reverse_linked_list(node)
    # chicken and egg problem: the first node.next needs to be None
    # step 2: make first node point to None
    node.next_1 = None


def reverse_linked_list(node):
    # # recursive: base case = no more nodes after, or: self.next_1 == None
    # because recursion creates a stack, it will go backwards from the end

    # stores value of this node
    temp = node

    # if there is a next...
    # (until base case of no next: if self.next_1 != None)
    if node.next_1:
        # this runs the recursive function on the 'next'
        reverse_linked_list(node.next_1)
        # and this sets that next node to connect to this node
        node.next_1.next_1 = temp


print("before")
print("node1 -> ", node1.next_1.value)
print("node2 -> ", node2.next_1.value)
print("node3 -> ", node3.next_1.value)
print("node4 -> ", node4.next_1.value)
# print(node5.next_1.value)

# reverse_linked_list(node1)
reverse_parent_function(node1)

print("after")

# print("node1 -> ", node1.next_1.value
print("node2 -> ", node2.next_1.value)
print("node3 -> ", node3.next_1.value)
print("node4 -> ", node4.next_1.value)
print("node5 -> ", node5.next_1.value)
