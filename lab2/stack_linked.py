class node:
    def __init__(self, data):
            self.data = data
            self.next = None


class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Linked List'''

    def __init__(self, capacity):
        '''Creates and empty stack with a capacity'''
        self.capacity = capacity
        self.head = None
        self.num_items = 0

    def is_empty(self):
        '''Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == 0

    def is_full(self):
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''
        return self.capacity == self.num_items

    def push(self, item):
        '''If stack is not full, pushes item on stack.
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full():
            raise IndexError
        if self.is_empty():
            self.head = node(item)
            self.num_items += 1
        else:
            next_node = node(item)
            temp = self.head.next
            next_node.next = temp
            self.head.next = next_node
            self.num_items += 1

            # if self.head:
            #     temp = self.head.next
            #     self.head.next = next_node
            #     next_node.next = temp
            # else:
            #     self.head = next_node
            #self.num_items += 1


    def pop(self):
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError
        else:
            if self.num_items == 1:
                self.num_items -= 1
                return self.head.data
            else:
                self.num_items -= 1
                item = self.head.next.data
                self.head.next = self.head.next.next
                return item


    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError

        else:
            if self.head.next: #if the next head exists; there's a value
                return self.head.next.data
            else:
                return self.head.data

    def size(self):
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''
        return self.num_items