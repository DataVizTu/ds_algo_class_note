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

queue = Queue()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)

print(queue.size_queue)
        
