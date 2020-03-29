from doubly_linked_list import DoublyLinkedList

# moveing nodes and pointers
# making class: least recently used cache


class LRUCache:  # create LRUCache class
    # the main class-methods (functions) are:
    # - self.get(key)
    # - self.set(key, value)

    # constructor method (function)
    def __init__(self, size_limit=10):
        # attributes
        self.size_limit = size_limit  # the max number of nodes it can hold
        self.current_size = 0  # the current number of nodes it holds
        # doubly-linked list holds key-value entries in correct LRU_order_DLL
        self.LRU_order_DLL = DoublyLinkedList()
        # Hash Table (python dict is a hash table)
        # storage_dict_dict provides fast access to every node stored in cache
        self.storage_dict = {}

        # # structure example:
        #
        # # the key of the dic is the entry key
        # # the value of the dict is the whole key_value_tuple
        # key_value_tuple = self.storage_dict[key]
        # key_value_tuple.value = (key, value)
        #
        # # the same key_value_tuple is what is in the DLL
        # self.LRU_order_DLL.move_to_end(key_value_tuple)
        # # or like this
        # self.LRU_order_DLL.add_to_tail((key, value))
        #
        # # the the dict-value(which is the tuple) can be
        # # directly swapped with the DLL 'value'
        # self.storage_dict[key] = self.LRU_order_DLL.tail
        #
        # # so be careful, because "value" is usually a tuple
        # # that contains both key and value
        #
        # # e.g. where you "get the value from the value"
        # # where you slice the key-value-tuple to get
        # # just the value
        # return key_value_tuple.value[1]

    # hit the cache:
    # see if item is in cache
    # return value if so
    def get(self, key):
        # "miss"
        # Key is not in cache -- return none
        if key not in self.storage_dict:
            return None

        # "hit"
        # note: you must update the LRU list as well as get your target
        else:
            # key is in cache
            # move it to most recently used
            #
            # set 'key_value_tuple' variable to be
            # the whole dictionary_key_and_value OOP-object
            # being searched for
            key_value_tuple = self.storage_dict[key]
            # move that key_value_tuple/object to the
            # 'most_recent' end of the LRU DLL-list
            self.LRU_order_DLL.move_to_end(key_value_tuple)

            # because the value (the target of the search)
            # is stores as a tuple (key, value)
            # you can get the second item by a slice -> tuple[1]
            return key_value_tuple.value[1]

    # add item to cache
    def set(self, key, value):
        # first check to see if the item is there
        # so that you don't duplicate the record.
        # Note: the key may be the same, needing an updated value!

        # if item exists (already)
        # Q: is this really checking for the value being the same?
        if key in self.storage_dict:
            # set variable to be the dic-object
            # corresponding to the input key
            key_value_tuple = self.storage_dict[key]
            # this overwrites/updates the dict
            key_value_tuple.value = (key, value)
            # this updates the DLL
            # move to tail (most recently used)
            self.LRU_order_DLL.move_to_end(key_value_tuple)
            return

        # check to see if the size limit is maxed out.
        # if current_size is at size_limit
        # drop the oldest item...
        # note: both dict and DLL must be modified (oldest entry dropped)
        if len(self.LRU_order_DLL) == self.size_limit:
            # evict the oldest entry
            # get the 'key' or 'index' from the tuple
            # of the oldest entry (set to varible)
            index_of_oldest = self.LRU_order_DLL.head.value[0]
            # delete dictionary with corresponding key
            del self.storage_dict[index_of_oldest]
            # drop the oldest item from the DLL
            # here 'oldest' is head
            self.LRU_order_DLL.remove_from_head()

        # Add the new entry:
        # add to LRU_order_DLL
        # here newest is 'tail'
        self.LRU_order_DLL.add_to_tail((key, value))
        # add to storage_dict
        self.storage_dict[key] = self.LRU_order_DLL.tail


# from doubly_linked_list import DoublyLinkedList

# Overview:
#
# this form of ring buffer
# does not delete files unless they are over-written by new ones
# e.g. even printed files remain inside to be printed again
# and new files are continually written as in a ring


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # self.current = None
        # uses DLL for storage

        # if ring is full
        self.fullness_flag = False
        # for the LRU cache
        # the main class-methods (functions) are:
        # - self.get(key)
        # - self.set(key, value)
        self.lru_cache = LRUCache(capacity)
        # keeps track of input
        self.head_pointer = 0
        self.storage = self.lru_cache.LRU_order_DLL

    def append(self, item):

        # whether or not item is there already, 'set' the item:
        # this will update the item
        self.lru_cache.set(item, item)

        # update list pointer, but only if it's a new item...
        if self.lru_cache.get(item) is not None:
            self.head_pointer += 1

            # update fullness flag
            if self.head_pointer >= self.capacity:
                self.fullness_flag = True

            # reset/update ring head pointer
            if self.head_pointer > self.capacity:
                self.head_pointer = 1

    def get(self):

        # print everything in the LRU cache
        #
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # First check if buffer is empty:
        # note: the pointer is only at zero before anything is entered
        # so you do not need to also check fullness_flag
        #
        # if empty, then cannot read
        if self.head_pointer == 0:  # and self.fullness_flag is False:
            # do nothing (if empty)
            pass

        else:
            # set mask to be
            # at first
            # the head node in the LRU_order_DLL
            node = self.lru_cache.LRU_order_DLL.head

            # if not full
            if self.fullness_flag is False:
                for i in range(self.head_pointer):
                    # add each item in the DLL
                    # only one part of the tuple is needed
                    list_buffer_contents.append(node.value[0])
                    # increment if exists
                    if node.next:
                        node = node.next

            # if full
            elif self.fullness_flag is True:
                for i in range(self.capacity):
                    # add each item in the DLL
                    # only one part of the tuple is needed
                    list_buffer_contents.append(node.value[0])
                    # increment if exists
                    if node.next:
                        node = node.next

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
