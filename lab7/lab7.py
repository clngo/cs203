class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

#1st: Create a binary tree
class BST:
    def __init__(self):
        self.root = None

    def add(self, num:int):
        if self.root is None:
            self.root = Node(num)
        else:
            self.addhelper(self.root, num)

    def addhelper(self, nroot: Node, num:int):
        if nroot is None: #base case
            return Node(num)
        elif num < nroot.data:  # new value is less than current, go left
            nroot.left = self.addhelper(nroot.left, num)
            return nroot
        else:
            nroot.right = self.addhelper(nroot.right, num)
            return nroot

    # 2nd Method: Recursive
    def recursive_preorderTraversal(self) -> list[int]:
        return self.preorderhelper(self.root)

    def preorderhelper(self, nroot:Node) -> list[int]:
        if nroot:
            return [nroot.data] + self.preorderhelper(nroot.left) + self.preorderhelper(nroot.right)
        else:
            return []

    def recursive_inorderTraversal(self) -> list[int]:
        return self.inorderhelper(self.root)

    def inorderhelper(self, eroot: Node):
        if eroot:
            return self.inorderhelper(eroot.left) + [eroot.data] + self.inorderhelper(eroot.right)
        else:
            return []

    def recursive_postorderTraversal(self) -> list[int]:
        return self.postorderhelper(self.root)

    def postorderhelper(self, eroot: Node):
        if eroot:
            return self.postorderhelper(eroot.left) + self.postorderhelper(eroot.right) + [eroot.data]
        else:
            return []

    # 3rd Method: Non-Recursive
    def preorderTraversal(self) -> list[int]:
        result = []
        stck = []
        temp = self.root
        while temp or stck:
            if temp:
                result.append(temp.data)  # put it in the list, preorder
                stck.append(temp)
                temp = temp.left  # traverse
            else:  # no root, then go back and to the right
                temp1 = stck.pop()
                temp = temp1.right
        return result

    def inorderTraversal(self) -> list[int]:
        result = []
        stck = []
        tempr = self.root
        while tempr or stck:
            if tempr:
                stck.append(tempr)
                tempr = tempr.left
            else:  # no root, but there's still something in the stack
                temp1 = stck.pop()  # goes back from the stack
                result.append(temp1.data)  # include this value
                tempr = temp1.right  # traverse again
        return result

    def postorderTraversal(self) -> list[int]:
        result = []
        stck = []
        tempr = self.root
        while True:
            while tempr is not None:
                stck.append(tempr)
                stck.append(tempr)
                tempr = tempr.left

            if len(stck) == 0:
                return result

            tempr = stck.pop()
            if len(stck) > 0 and stck[-1] == tempr:
                tempr = tempr.right
            else:
                result.append(tempr.data)
                tempr = None


test1 = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
test1_1 = BST()
for num in test1:
    test1_1.add(num)
print(f"recursive preorder: {test1_1.recursive_preorderTraversal()}")
print(f"iterative preorder: {test1_1.preorderTraversal()}\n")

print(f"recursive inorder: {test1_1.recursive_inorderTraversal()}")
print(f"iterative inorder: {test1_1.inorderTraversal()}\n")

print(f"recursive postorder: {test1_1.recursive_postorderTraversal()}")
print(f"iterative postorder: {test1_1.postorderTraversal()}\n")

#test2 = [43, 15, 60, 8, 30, 50, 82, 20, 35, 70]
test2 = [5, 6, 3, 7, 4, 2]
test2_1 = BST()
for num in test2:
    test2_1.add(num)

print(f"recursive preorder: {test2_1.recursive_preorderTraversal()}")
print(f"iterative preorder: {test2_1.preorderTraversal()}\n")

print(f"recursive inorder: {test2_1.recursive_inorderTraversal()}")
print(f"iterative inorder: {test2_1.inorderTraversal()}\n")

print(f"recursive postorder: {test2_1.recursive_postorderTraversal()}")
print(f"iterative postorder: {test2_1.postorderTraversal()}")


test3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
test3_1 = BST()
for num in test3:
    test3_1.add(num)
print("\nTEST 3")
print(f"recursive preorder: {test3_1.recursive_preorderTraversal()}")
print(f"iterative preorder: {test3_1.preorderTraversal()}\n")

print(f"recursive inorder: {test3_1.recursive_inorderTraversal()}")
print(f"iterative inorder: {test3_1.inorderTraversal()}\n")

print(f"recursive postorder: {test3_1.recursive_postorderTraversal()}")
print(f"iterative postorder: {test3_1.postorderTraversal()}")