class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of
list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.dummy = Node(None) #dummy node
        self.dummy.prev = self.dummy.next = self.dummy #Dummy next and prev is itself

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        return self.dummy.next == self.dummy.prev == self.dummy


    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''
        new_node = Node(item)
        if self.is_empty(): #no nodes
            new_node.next = new_node.prev = self.dummy
            self.dummy.next = self.dummy.prev = new_node
        else: #at least has 1 node
            temp = self.dummy.next
            found = False
            while temp != self.dummy:
                if item < temp.item: #if new < curr: new = curr.prev & new.next = curr.next
                    temp.prev.next = new_node #before curr.next is new
                    new_node.prev = temp.prev
                    temp.prev = new_node #curr.prev = new
                    new_node.next = temp #new.next = cur
                    found = True
                    break
                else: #continue
                    temp = temp.next
            if not found: #if cycled through everything, but no new node, add it at the end
                self.dummy.prev.next = new_node #last node.next = new
                new_node.prev = self.dummy.prev  #new.prev = oldtail
                new_node.next = self.dummy #new.next = dummy
                self.dummy.prev = new_node #new tail = new node



    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was
in the list)
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        if self.is_empty():
            return False
        temp = self.dummy.next
        while temp != self.dummy:
            if temp.item == item:  # if new < curr: new = curr.prev & new.next = curr.next
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return True
            else:  # continue
                temp = temp.next
        return False

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of
list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        if self.is_empty():
            return None
        index = 0
        temp = self.dummy.next
        while temp != self.dummy:
            if temp.item == item:  # if new < curr: new = curr.prev & new.next = curr.next
                return index
            else:  # continue
                temp = temp.next
                index += 1
        return None


    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if self.is_empty() or index < 0:
            raise IndexError
        idx = 0
        temp = self.dummy.next
        while temp != self.dummy:
            if idx == index:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return temp.item
            else:  # continue
                temp = temp.next
                idx += 1
        raise IndexError

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''

        if self.is_empty():
            return False
        #start at dummy.next
        return self.searchhelper(self.dummy.next, item)

    def searchhelper(self, enode, item):
        if enode == self.dummy: #stop recursion when reached the dummy node
            return False
        if enode.item == item: #yay it's there
            return True
        else: #not dummy but not item, continue down the nodes
            return self.searchhelper(enode.next, item)


    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        if self.is_empty():
            return []
        lst = []
        temp = self.dummy.next
        while temp != self.dummy:
            lst.append(temp.item)
            temp = temp.next
        return lst

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using
recursion

           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        if self.is_empty():
            return []
        return self.python_list_reversed_helper(self.dummy.prev)

    def python_list_reversed_helper(self, enode) -> list:
        if enode == self.dummy:
            return []
        else:
            return [enode.item] + self.python_list_reversed_helper(enode.prev)


    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        if self.is_empty():
            return 0
        return self.sizehelper(self.dummy.next)

    def sizehelper(self, enode):
        if enode == self.dummy:
            return 0
        else:
            return 1 + self.sizehelper(enode.next)
