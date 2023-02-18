class Stack():
    def __init__(self):
        self.list = []    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    def push(self, value):
        self.list.append(value)
    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list.pop()
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list(len[self.list]-1)
    def delete(self):
        self.list = None
    
class Queue():
    def __init__(self):
        self.list = []
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    def enqueue(self, value):
        self.list.append(value)
    def dequeue(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list.pop(0)
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list(0)
    def delete(self):
        return self.list == None
    
class QueueLimited():
    def __init__(self, maxSize):
        self.list = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1
    def isFull(self):
        if self.top +1 == self.start:
            return True
        elif self.start == 0 and self.top +1 == self.maxSize:
            return True
        else:
            return False
    def isEmpty(self):
        if self.top == -1:
            return True
        else: 
            return False
    def peek(self):
        if self.isEmpty():
            return "There's no element on the Queue"
        else: 
            return self.items[self.start]
    def delete(self):
        self.items = self.maxSize * [None]
        self.start = -1
        self.top = -1
    def enqueue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top +1 == self.maxSize:
                self.top = 0
            else:
                self.top +1
                if self.start == -1:
                    self.start = 0
        self.items[self.top] = value
    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start +=1
            self.items[start] = None
            return firstElement