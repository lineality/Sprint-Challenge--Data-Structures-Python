class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    # def reverse_list(self, node, prev):
    #     # You must use recursion for this solution
    #     pass

    def reverse_linked_list(self, node):
        # # recursive: base case = no more nodes after, or: self.next_node == None
        # because recursion creates a stack, it will go backwards from the end

        # stores value of this node
        temp = node

        # if there is a next...
        # (until base case of no next: if self.next_node != None)
        if node.next_node:
            # this runs the recursive function on the 'next'
            self.reverse_linked_list(node.next_node)
            # and this sets that next node to connect to this node
            node.next_node.next_node = temp

    def reverse_list(self, node, prev=None):

        if node:
            # step 1: run recursive reverse_order function
            self.reverse_linked_list(node)
            # chicken and egg problem: the first node.next needs to be None

            if node.next_node:
                # step 2: make first node point to None
                node.next_node = None

            else:
                return None
        else:
            return None
