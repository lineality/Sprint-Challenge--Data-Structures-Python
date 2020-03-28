from doubly_linked_list import DoublyLinkedList

# Overview:
#
# this form of ring buffer
# does not delete files unless they are over-written by new ones
# e.g. even printed files remain inside to be printed again
# and new files are continually written as in a ring


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        # uses DLL for storage
        self.storage = DoublyLinkedList()
        # if ring is full
        self.fullness_flag = False
        # keeps track of input
        self.head_pointer = 0

    def append(self, item):
        # there are two basic modes here:
        # before the ring is full, and after the ring is fullness_flag
        # before the ring is full, items are added to the tail_pointer
        # after the ring is full, then over-writing begins

        # Steps:

        # increment head_pointer
        self.head_pointer += 1

        # update/reset head_pointer if at ring-end
        # if pointer is moved one past the end (capasity)
        # then move the head pointer back to 1
        if self.head_pointer is self.capacity + 1:

            # reset head-counter
            self.head_pointer = 1

        # 1. is the ring full yes? is fullness_flag True?
        if self.fullness_flag is True:
            # if full:
            # overwrite value in ring-fashion
            # set starting point
            node = self.storage.head

            # if the pointer is at 1, no incrementing is needed
            if self.head_pointer == 1:
                # set that ring-wise value to be the item
                self.storage.head.value = item

            # but if the pointer is past 1, increment:
            elif self.head_pointer > 1:
                # step through each node in the linked list
                for i in range(self.head_pointer - 1):
                    node = node.next
                # set that ring-wise value to be the item
                node.value = item

        else:  # if not full, just add to tail
            # # 2. if not full:
            # elif self.fullness_flag == False:

            # add to tail
            self.storage.add_to_tail(item)  # list[headpointer]=new_data_input

        # check to see if new size is "full"
        if self.head_pointer is self.capacity:  # head_pointer == tail_pointer?
            self.fullness_flag = True

    def get(self):
        # again, full or not full rings will work differently
        # a not full ring only prints up to the pointer
        # a full ring prints all capacity
        #
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # this will print from head to tail
        # which evidently is what
        # "in their given order" means, in some universe
        # this ring will not however delete anything
        # nore will it print None values

        # First check if buffer is empty:
        # note: the pointer is only at zero before anything is entered
        # so you do not need to also check fullness_flag
        #
        # if empty, then cannot read
        if self.head_pointer == 0:  # and self.fullness_flag is False:
            # do nothing (if empty)
            pass

        # if Ring is full: print to capacity
        if self.fullness_flag is True:
            # set starting point
            node = self.storage.head

            # step through each node in the linked list
            for i in range(self.capacity):

                # check if value is not "None"
                if node is not None:
                    # if not None, add that to the print-list
                    list_buffer_contents.append(node.value)
                node = node.next

        # if ring not full: print just to head_pointer
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

        # for any outcome, return the list of results
        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
