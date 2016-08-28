"""Question 1 - Assignment 1
   Node class implementation
   Python Version 2.x"""

class MyNode:

    def __init__(self, v, l, r, p):
        self.value = v
        self.left = l
        self.right = r
        self.parent = p

    def getChildren(self):
        return [self.left, self.right]





















"""
Tests:

myNode = Node(value, left, right, parent)

print myNode.getChildren( ) #should return [leftChild, rightChild]

print myNode.value

"""
