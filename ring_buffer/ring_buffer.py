from doubly_linked_list import DoublyLinkedList


# from doubly_linked_list import DoublyLinkedList

# this form of ring buffer
# does not delete files unless they are over-written by new ones
# e.g. even printed files remain inside to be printed again


# from doubly_linked_list import DoublyLinkedList

# this form of ring buffer
# does not delete files unless they are over-written by new ones
# e.g. even printed files remain inside to be printed again
# and new files are continually written as in a ring

# from doubly_linked_list import DoublyLinkedList

# this form of ring buffer
# does not delete files unless they are over-written by new ones
# e.g. even printed files remain inside to be printed again
# and new files are continually written as in a ring


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.fullness_flag = False
        # keeps track of input
        self.head_pointer = 0
        # # keeps track of ouput
        # self.tail_pointer = 0

    def append(self, item):
        # first check to see how much room there is:

        # increment head_pointer
        self.head_pointer += 1

        # update head_pointer if at ring-end
        # if pointer is moved one past the end
        # move it back to 1
        if self.head_pointer is self.capacity + 1:

            # reset head-counter
            self.head_pointer = 1

        # 1. is it full? is fullness_flag True?
        if self.fullness_flag == True:
            # if full: new element cannot be added
            # until old history deleted
            # self.storage.remove_from_head()

            # overwrite value in ring-fashion
            # set starting point
            node = self.storage.head

            if self.head_pointer is 1:
                # set that ring-wise value to be the item
                self.storage.head.value = item

            elif self.head_pointer > 1:
                # step through each node in the linked list
                for i in range(self.head_pointer - 1):
                    node = node.next
                # set that ring-wise value to be the item
                node.value = item

        else:  # if not full
            # # 2. if not full:
            # elif self.fullness_flag == False:

            # add to tail
            self.storage.add_to_tail(item)  # list[headpointer] = new_data_input

        # check to see if new size is "full"
        if self.head_pointer is self.capacity:  # head_pointer == tail_pointer?
            self.fullness_flag = True

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # this will print from head to tail
        # which evidently is what
        # "in their given order" means, in some universe
        # this will not however delete anything
        # nore will it print None values

        # First check if buffer is empty:
        # if empty, then cannot read
        if self.head_pointer == 0:
            # do nothing (if empty)

            pass

        if self.fullness_flag == True:
            # set starting point
            node = self.storage.head

            # step through each node in the linked list
            for i in range(self.capacity):

                # check if value is not "None"
                if node:
                    list_buffer_contents.append(node.value)
                node = node.next

        # if not empty:
        # only for not-None items
        else:
            # for i in self.capacity:

            # set starting point
            node = self.storage.head

            # step through each node in the linked list
            for i in range(self.head_pointer):

                # check if value is not "None"
                if node:
                    list_buffer_contents.append(node.value)
                node = node.next

        # 	data_to_read = ring_butter[tail_pointer]
        # 	tail_pointer += 1

        return list_buffer_contents

    # # auto-populate ring with null values
    # for i in range (self.capacity)


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
