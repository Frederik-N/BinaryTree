# Building a Binary tree

class Node:
    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.value = value
class BinaryTree:
    def __init__(self, filename):
        self.root = None
    
    def addNode(self, node, value):
        if(node==None):
            self.root = Node(value)
        else:
            if(value<node.value):
                if(node.left==None):
                    node.left = Node(value)
                else:
                    self.addNode(node.left, value)
            else:
                if(node.right==None):
                    node.right = Node(value)
                else:
                    self.addNode(node.right, value)

    def __printInOrder(self, node):
        if(node!=None):
            self.__printInOrder(node.left)
            print(node.value)
            self.__printInOrder(node.right)

    def print(self):
        return self.__printInOrder(self.root)

    def createTree(self, filename):
        binaryTree = self.__makeBinaryTree(filename)
        return binaryTree

    #save the data of triangle in a binary tree
    def __makeBinaryTree(self, filenameTriangle):
        data = open(filenameTriangle,"r")
        if(data.mode == 'r'):
            datastring = data.read()
        datalist = datastring.split('\n')

        newlist = []
        for x in range(len(datalist)):
            for y in datalist[x].split(" "):
                self.addNode(self.root,y)
        return self

#actual class to solve the problem
class MaxPathSum:
    def __init__(self, filenameTriangle):
        self.filename = filenameTriangle
        self.binaryTree = self.createBinaryTree()

    def createBinaryTree(self):
        bt = BinaryTree(self.filename)
        return bt.createTree(self.filename)
    
    # actual method that solves the problem
    def __findMaxSum(self):
        return "Solution is %s" % 2

    # run method to solve the MaxPathSum problem for this instance
    def solveMaxPath(self):
        binaryTree = self.createBinaryTree()
        return self.__findMaxSum()