from listNode import ListNode

class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__numItems = 0
        
        
    def insert(self, i, newItem):
        if i >= 0 and i <= self.__numItems:
            prev = self.__getNode(i-1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1
        else:
            print("index", i, ": out of bound in insert()")
            
    def __getNode(self, i):
        curr = self.__head
        for index in range(i+1):
            curr = curr.next
            
        return curr
    
    def append(self, newItem):
        prev = self.__getNode(self.__numItems-1)
        newNode = ListNode(newItem, None)
        prev.next = newNode
        self.__numItems += 1
    
    def pop(self, i):
        if i >= 0 and i <= self.__numItems - 1:
            prev = self.__getNode(i-1)
            curr = prev.next
            prev.next = curr.next
            retItem = curr.item
            self.__numItems -= 1
            return retItem
        else:
            return None
    
    def remove(self, x):
        prev, curr = self.__findNode(x)
        if curr != None:
            prev.next = curr.next
            self.__numItems -= 1
            
    def __findNode(self, x):
        prev = self.__head
        curr = prev.next
        while curr != None:
            if curr.item == x:
                return prev, curr
            else:
                prev = curr
                curr = curr.next
        return None, None
    
    def get(self, i):
        if self.isEmpty():
            return None
        if i >= 0 and i <= self.__numItems - 1:
            return self.__getNode(i).item
        else:
            return None
    
    def index(self, x):
        curr = self.__head.next
        for index in range(self.__numItems):
            if curr.item == x:
                return index
            else:
                curr = curr.next
                
        return -12345
    
    def isEmpty(self):
        return self.__numItems == 0
    
    def size(self):
        return self.__numItems
    
    def clear(self):
        self.__head = ListNode("dummy", None)
        self.__numItems = 0
    
    def count(self, x):
        cnt = 0
        curr = self.__head.next
        while curr != None:
            if curr.item == x:
                cnt += 1
            curr = curr.next
        return cnt
    
    def extend(self, a):
        for index in range(a.size()):
            self.append(a.get(index))
    
    def copy(self):
        a = LinkedListBasic()
        for index in range(self.__numItems):
            a.append(self.get(index))
            
        return a
    
    def reverse(self):
        a = LinkedListBasic()
        for index in range(self.__numItems):
            a.insert(0, self.get(index))
        self.clear()
        for index in range(a.size()):
            self.append(a.get(index))
    
    def sort(self):
        
        a = []
        for index in range(self.__numItems):
            a.append(self.get(index))
        a.sort()
        self.clear()
        for index in range(len(a)):
            self.append(a[index])
            
    def printList(self):
        curr = self.__head.next
        while curr != None:
            print(curr.item, end=" ")
            curr=curr.next
        print()

    
    
# Test Code
list = LinkedListBasic()
list.append(30); list.insert(0, 20)
a = LinkedListBasic()
a.append(4); a.append(3); a.append(3); a.append(2); a.append(1)
list.extend(a)
list.reverse()
list.pop(0)
print("count(3):", list.count(3))
print("get(2):", list.get(2))
list.printList()