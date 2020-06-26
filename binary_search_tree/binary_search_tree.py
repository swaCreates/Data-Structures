"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value) #recursion
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value) #recursion

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif self.value < target:
            if self.right is None: 
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        if self.left is not None:
            self.left.in_order_print(node)
        if self.right is not None:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node is None:
            return
        # create a queue for nodes
        queue = Queue()
        # add the first node to the queue
        queue.enqueue(node)
        # while queue is not empty
        while len(queue.storage) is not 0:
            # remove the first node from the queue
            curr_node = queue.dequeue()
            # print the removed node 
            print(curr_node)
            # add all children into the queue
            if curr_node.left is not None:
                queue.enqueue(curr_node.left)
            if curr_node.right is not None:
                queue.enqueue(curr_node.right)
       

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node is None:
            return
        # create a stack for nodes
        stack = Stack()
        # add the first node to the stack
        stack.push(node)
        # while the stack is not empty
        while len(stack.storage) is not 0:
            # get the current node from the top of the stack
            curr_node = stack.storage.pop(0)
            # print that node
            print(curr_node)
            # add all children to the stack
            if curr_node.left is not None:
                stack.push(curr_node.left)
            if curr_node.right is not None:
                stack.push(curr_node.right)
        

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
