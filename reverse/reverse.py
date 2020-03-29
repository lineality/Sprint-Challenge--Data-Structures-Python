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

    # You must use recursion for this solution

    # This function reverses the sequence of a singly linked list
    # and satisfies the followed exceptional cases:
    # - only an empty node is input (returns None)
    # - only one node is put in (does nothing)
    # - both parameters are correctly filled (works)
    # - the second parameter is filled with None
    #   even though there was a second parameter to use
    #
    # There are two functions. The helper function handles
    # exceptional inputs, but the recursive functions works
    # when used alone if the input is valid.
    #
    #  Helper function for invalid input exceptions:
    def reverse_list(self, node, prev):

        # if only an empty node is input
        # outputs: None
        if node is None:
            return None

        # if there is only one node:
        # so node exists but node.next_node does not, then
        # pass: do nothing
        elif node is not None and node.next_node is None:
            pass

        # "Missing Parameter" input:
        # if there are several nodes but the "prev" input
        # is left blank, set "prev" to be "prev" (self.head.next_node)
        # and then run the recursive function
        elif node is not None and prev is None:
            prev = self.head.next_node

            # run recursive function
            self.reverse_list2(node.next_node, prev.next_node)

    # Recursive function that works alone with valid input
    def reverse_list2(self, node, prev):

        # save temp value of node
        temp_node = node

        # loops through as long as there is a previous node
        if prev is not None:
            # recursively calls function, creating a stack
            # until base case,
            self.reverse_list2(node.next_node, prev.next_node)
            # and then in reverse order re-assigning the
            # node relationships (changning direction)
            # what was previous becomes next
            prev.next_node = temp_node

        # because the head needs to be assigned
        # directly in "this" class structure
        else:
            self.head = node

    # # note: the recursive function is very simple, without all the exeptions
    # def reverse_list(node, prev):
    #     temp_node = node
    #     if prev != None:
    #         reverse_list(node.next_node, prev.next_node)
    #         prev.next_node = temp_node
    #     else:
    #         Tom.head = node

