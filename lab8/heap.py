class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class MaxHeap:
    def __init__(self, capacity=50):
        self.size = 0
        self.capacity = capacity
        self.heapl = [None] * (capacity+1)

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in
    the heap "item" can be any primitive or ***object*** that can be compared with other items using the < operator'''
        self.size += 1
        if self.size > self.capacity:
            return False
        self.heapl[self.size] = item
        self.perc_up(self.size)
        return True


    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.is_empty():
            return
        return self.heapl[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
        returns None if the heap is empty'''
        result = self.heapl[1]
        self.heapl[1] = self.heapl[self.size]
        self.size -= 1
        self.heapl.pop()
        self.perc_down(1)
        return result


    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        return self.heapl[1:self.size+1]

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from
        the items in alist using the bottom-up construction method. If the capacity of the current heap is less
        than the number of items in alist, the capacity of the heap will be increased to accommodate the items in alist'''
        idx = len(alist) // 2
        self.size = len(alist)
        self.heapl = [None] + alist[:]
        if self.capacity > len(alist):
            self.heapl += [None] * (self.capacity - len(alist))
            # for i in range(len(alist), self.capacity):

        while idx > 0:
            self.perc_down(idx)
            idx -= 1
    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return self.size == 0

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.size == (len(self.heapl)-1)

    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold 1 less than the number of entries that the
        array allocated to hold the heap can hold'''
        return self.capacity

    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.size

    def perc_down(self,i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while (i * 2) <= self.size:
            #find the index of the bottom of the tree (lowest)
            if (i*2+1) > self.size: #finding the right child
                max_idx = i * 2
            else:
                if self.heapl[i*2] < self.heapl[i*2+1]:
                    max_idx = i * 2 + 1
                else:
                    max_idx = i * 2
            if self.heapl[i] < self.heapl[max_idx]: #swap
                self.heapl[i], self.heapl[max_idx] = self.heapl[max_idx], self.heapl[i]
            i = max_idx

    def perc_up(self,i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while (i // 2) > 0:
            if self.heapl[i] > self.heapl[i//2]:
                self.heapl[i], self.heapl[i//2] = self.heapl[i//2], self.heapl[i]
            i = i // 2

    def heap_sort_ascending(self,alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.build_heap(alist)
        while not self.is_empty():
            alist[self.get_size()] = self.dequeue()
        return alist

