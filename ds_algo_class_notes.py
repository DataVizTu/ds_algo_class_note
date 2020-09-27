# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:38:54 2020
@author: iPanda
"""

##array implementation

#random indexing: indexes starts with 0

my_list = [2,3,4,5,6,10,55,70]

array_el_3 = my_list[3]


##linear search O(N)

max_num = my_list[0]

for num in my_list:
    if num > max_num:
        max_num = num
        
        
##linked list
class Node:
    
    def __init__(self, data):
        self.data = data
        self.nextNote = None

class LinkedList:
    
    
    #This is why we like linked lists / O(1)
    def __init__ (self):
        self.head = None
        self.numOfNodes = 0
        
        
    def insert_start(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)
        
        
        if  not self.head:
            self.head = new_node
        else:
            new_node.nextNote = self.head
            self.head = new_node
           
    #linear running time O(N)
    def insert_end(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)
        actual_node =  self.head
        
        while actual_node.nextNote is not None:
            actual_node = actual_node.nextNote
        
        actual_node.nextNote = new_node

    def remove(self, data):

        if self.head is None:
            return 
        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.nextNote

        #item is not present
        if actual_node is None:
            return

        if previous_node is None:
            self.head = actual_node.nextNote
        else:
            previous_node.nextNote = actual_node.nextNote


     #O(1)  
    def size_of_linkedList(self):
        return self.numOfNodes
    
    #O(N)
    def traverse(self):
        
        actual_node = self.head
        
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNote
            

# linked_list = LinkedList()
# linked_list.insert_start(4)
# linked_list.insert_start(2)
# linked_list.insert_end(3)
# linked_list.insert_end(5)
# linked_list.insert_end(1000.8)
# linked_list.insert_end('Adam')

# linked_list.traverse()
# linked_list.remove('Adam')
# print("-----")
# linked_list.traverse()


##Stack Implementation, LIFO

class Stack:

    def __init__(self):
        self.stack = []

    #insert item on the stack // O(1)

    def push(self, data):
        self.stack.append(data)

    #remove and return the last item we have inserted (LIFO) // O(1)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    # peek: return the last item without removing it // O(1)

    def peek(self):
        return self.stack[-1]

     #O(1)
    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)

# stack = Stack()
# print(stack.push(4))
# print(stack.push(5))
# print(stack.push(6))

# print(stack.stack_size())
# print(stack.pop())
# print(stack.stack_size())
# print(stack.peek())
            
#queue implementation FIFO

class Queue:

    def __init__(self):
        self.queue = []


    # O(1) running time
    def is_empty(self):
        return self.queue == []  


    #O(1) enqueue
    def enqueue (self, data):
        self.queue.append(data)

    #O(N) dequeue
    def dequeue(self):
        if self.size_queue() != 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            return -1

    #O(1) peek
    def peek(self):
        return self.queue[0]

    def size_queue(self):
        return len(self.queue)

# queue = Queue()
# print(queue.enqueue(1))
# print(queue.enqueue(3))
# print(queue.enqueue(5))

# print(queue.size_queue())
# print(queue.dequeue())
# print(queue.size_queue())


#binary search tree implementation

class Node:

    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None 
        self.rightChild = None
        self.parent = parent
        
        
class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)


    #O(logN) = balanced tree
    def insert_node(self, data, node):
        #go to left subtree
        if data < node.data:
            if node.leftChild is not None:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)
        #go to right subtree
        else:
            if node.rightChild is not None:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)


     def remove_node(self, data, node):

        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.leftChild)
        elif data > node.data:
            self.remove_node(data, node.rightChild)
        else:

            if node.leftChild is None and node.rightChild is None:
                print("Removing a leaf node...%d" % node.data)

                parent = node.parent

                if parent is not None and parent.leftChild == node:
                    parent.leftChild = None
                if parent is not None and parent.rightChild == node:
                    parent.rightChild = None

                if parent is None:
                    self.root = None

                del node

            elif node.leftChild is None and node.rightChild is not None:  # node !!!
                print("Removing a node with single right child...")

                parent = node.parent

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                else:
                    self.root = node.rightChild

                node.rightChild.parent = parent
                del node

            elif node.rightChild is None and node.leftChild is not None:
                print("Removing a node with single left child...")

                parent = node.parent

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.leftChild
                    if parent.rightChild == node:
                        parent.rightChild = node.leftChild
                else:
                    self.root = node.leftChild

                node.leftChild.parent = parent
                del node

            else:
                print('Removing node with two children....')

                predecessor = self.get_predecessor(node.leftChild)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.rightChild:
            return self.get_predecessor(node.rightChild)

        return node

    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)


    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def get_min_value(self):
        if self.root:
            return get_min(self.root)

    def get_min(self, node):
        if node.leftChild:
            return self.get_min(node.leftChild)

        return node.data

    def get_max_value(self):
        if self.root:
            return get_max(self.root)

    def get_max(self, node):
        if node.rightChild:
            return self.get_max(node.rightChild)

        return node.data

    def traverse_in_order(self, node):

        if node.leftChild is not None:
            self.traverse_in_order(node.leftChild)
        
        print('%s' % node.data)

        if node.rightChild:
            self.traverse_in_order(node.rightChild)


bst = BinarySearchTree()
bst.insert(1)
bst.insert(5)
bst.insert(77)
bst.insert(10000)
bst.insert(100)
bst.insert(-6)


print(' min %d' % bst.get_min(bst.root))
bst.traverse()