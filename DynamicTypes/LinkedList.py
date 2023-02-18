from random import randint

class Node():
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.value)
    
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next 
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next 
        return result
    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self
    
class Circular():
    def __init__(self, valueNode):
        node = Node(valueNode)
        self.next = node
        self.head = node
        self.tail = node
        
class Doubly():
    def __init__(self, valueNode):
        node = Node(valueNode)
        self.next = None
        self.prev = None
        self.head = node
        self.tail = node