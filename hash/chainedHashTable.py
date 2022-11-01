from circularLinkedList import CircularLinkedList

class ChainedHashTable:
    def __init__(self, n):
        self.__table = [CircularLinkedList() for i in range(n)]
        self.__numItems = 0;
        
    def __hash(self, x):
        return x % len(self.__table)
    
    def insert(self, x):
        slot = self.__hash(x)
        self.__table[slot].insert(0,x)
        self.__numItems += 1
        
    def search(self, x):
        slot = self.__hash(x)
        if self.__table[slot].isEmpty():
            return None
        else:
            head = prev = self.__table[slot].getNode(-1)
            curr = prev.next
            while curr != head:
                if curr.item == x:
                    return curr
                else:
                    prev = curr; curr = curr.next
            return None
        
    def delete(self, x):
        slot = self.__hash(x)
        success = self.__table[slot].remove(x)
        if success != None:
            self.__numItems -= 1
    
    def isEmpty(self):
        return self.__numItems == 0
    
    def clear(self):
        for i in range(len(self.__table)):
            self.__table[i] = CircularLinkedList()
        self.__numItems = 0
        

# Test Code
h = ChainedHashTable(7)
h.insert(10)
h.insert(21)
h.insert(20)
h.insert(20)
h.insert(5)
h.insert(12)
h.insert(19)
h.insert(80)
h.insert(32)
h.delete(20)
h.delete(44)

item = 21
slot = h.search(item)
if slot == None:
    print("Search Failed")
else:
    print("Search for ", item, " Successful at slot ",slot)