"""Question 3 - Assignment 1
   Stack implementation in python using a list
   Python version: 2.x"""


class Stack():

    #Create new stack"
    def __init__(self):
        self.newStack = []

    #Set len() definition
    def __len__(self):
        return len(self.newStack)

    def isEmpty(self):
        if len(self.newStack) == 0:
            return True
        else:
            return False

    def push(self, integer):
        return self.newStack.append(integer)

    def pop(self):
        if self.isEmpty() == True:
            return "Stack empty."
        else:
            return self.newStack.pop()

    def checkSize(self):
        return len(self.newStack)















"""
Tests needed to pass:

myStack = Stack()

myStack.push(5)

myStack.push(2)

myStack.pop()

myStack.checkSize()

When the stack is initialized, it should be empty.
"""
