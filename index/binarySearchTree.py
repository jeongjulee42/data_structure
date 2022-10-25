class TreeNode:
    def __init__(self, newItem, left, right):
        self.item = newItem
        self.left = left
        self.right = right
        

class BinarySearchTree:
    def __init__(self):
        self.__root = None
        
    def search(self, x):
        return self.__searchItem(self.__root, x)
    
    def __searchItem(self, tNode, x):
        if tNode == None:
            return None
        elif x == tNode.item:
            return tNode
        elif x < tNode.item:
            return self.__searchItem(tNode.left, x)
        else:
            return self.__searchItem(tNode.right, x)
        
    def insert(self, newItem):
        self.__root = self.__insertItem(self.__root, newItem)
        
    def __insertItem(self, tNode, newItem):
        if tNode == None:
            tNode = TreeNode(newItem, None, None)
        elif newItem < tNode.item:
            tNode.left = self.__insertItem(tNode.left, newItem)
        else:
            tNode.right = self.__insertItem(tNode.rignt, newItem)
        return tNode
        
    def delete(self, x):
        self.__root = self.__deleteItem(self.__root, x)
        
    def __deleteItem(self, tNode, x):
        if tNode == None:
            return None
        elif x == tNode.item:
            tNode = self.__deleteNode(tNode)
        elif x < tNode.item:
            tNode.left = self.__deleteItem(tNode.left, x)
        else:
            tNode.right = self.__deleteItem(tNode.right, x)
        return tNode
    
    def __deleteNode(self, tNode):
        if tNode.left == None and tNode.right == None:
            return None
        elif tNode.left == None:
            return tNode.right
        elif tNode.right == None:
            return tNode.left
        else:
            rtnItem, rtnNode = self.__deleteMinItem(tNode.right)
            tNode.item = rtnItem
            tNode.right = rtnNode
            return tNode
        
    def __deleteMinItem(self, tNode):
        if tNode.left == None:
            return tNode.item, tNode.right
        
        else:
            rtnItem, rtnNode = self.__deleteMinItem(tNode.left)
            tNode.left = rtnNode
            return rtnItem, tNode
        
    def isEmpty(self):
        return self.__root == self.NIL
    
    def clear(self):
        self.__root = self.NIL