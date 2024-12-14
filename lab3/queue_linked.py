class node:
    def __init__(self, item):
        self.data = item
        self.next = None


class Queue:
    '''Implements a link-based ,efficient first-in first-out Abstract Data Type'''
    def __init__(self, capacity:int):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.num_items = 0

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == 0

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == self.capacity

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full():
            raise IndexError
        else: #not full
            new_node = node(item)
            if self.is_empty():
                self.head = new_node
                self.tail = new_node
            else:
                temp = self.head
                temp.next = new_node
                self.head = new_node
            self.num_items += 1


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError
        else:
            item = self.tail.data
            self.tail = self.tail.next
            self.num_items -= 1
            return item


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items