class Queue_array:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type
       using a Python array (faked using a List)'''
    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0
        self.front = 0
        self.back = 0


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == 0


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        return self.capacity == self.num_items


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full():
            raise IndexError
        else:
            #print(f"back: {self.back}")
            if self.back >= self.capacity:
                #print("yes")
                self.back = 0
            self.items[self.back] = item
            self.back += 1
            self.num_items += 1


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError
        else:
            #print(f"front: {self.front}")
            if self.front >= self.capacity:
                self.front = 0
            tempitem = self.items[self.front]
            self.front += 1
            self.num_items -= 1
            return tempitem


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items