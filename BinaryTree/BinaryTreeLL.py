from DynamicTypes import QueueLinkedList as queue 

class TreeNode():
    def __init__(self, data, children):
        self.data = data
        self.children = children
    def __str__(self, level = 0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    def addChild(self, TreeNode):
        self.children.append(TreeNode)

# BINARY TREE WITH LINKED LIST
class TreeNode():
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "The binary tree does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Node exist"
            if (root.value.leftChild) is not None:
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild) is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Not found"
def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully inserted"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully inserted"
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode
def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)
def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "Binary Tree does not exist"
    else:
       customQueue = queue.Queue()
       customQueue.enqueue(rootNode) 
       while not(customQueue.isEmpty()):
           root = customQueue.dequeue()
           if root.value.data == node:
               dNode = getDeepestNode(rootNode)
               root.value.data = dNode.data
               deleteDeepestNode(rootNode, dNode)
               return "The node has been successfully deleted"
           if (root.value.leftChild is not None):
                    customQueue.enqueue(root.value.leftChild)
           if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
       return "Failed to delete"
def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "Binary Tree has been successfully deleted"

newBT =TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild
cola = TreeNode("Cola")
print(insertNodeBT(newBT, cola))
preOrderTraversal(newBT)
deepestNode = getDeepestNode(newBT)
print("-------------------")
newNode = getDeepestNode(newBT)
deleteDeepestNode(newBT, newNode)
preOrderTraversal(newBT)
print("-------------------")
deleteNodeBT(newBT, 'Hot')
levelOrderTraversal(newBT)
print("-------------------")
deleteBT(newBT)
levelOrderTraversal(newBT)