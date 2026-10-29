class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        
    def get(self, index: int) -> int:
        node = self.head
        while index > 0 and node is not None:
            node = node.next
            index -= 1
        return -1 if node is None else node.val

        
    def addAtHead(self, val: int) -> None:
        tmp = Node(val)
        tmp.next = self.head
        self.head = tmp
        if self.tail is None:
            self.tail = self.head
        
        print(self.get(3))
        

    def addAtTail(self, val: int) -> None:
        tmp = Node(val)
        if self.tail is None:
            self.head = self.tail = tmp
        else:
            self.tail.next = tmp
            self.tail = tmp

        

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            return self.addAtHead(val)
        
        prev = self.head
        index -= 1
        while index > 0:
            prev = prev.next
            index -= 1
        
        tmp = Node(val)
        tmp.next = prev.next
        prev.next = tmp
        if tmp.next is None:
            self.tail = tmp

    def deleteAtIndex(self, index: int) -> None:
        if index <= 0:
            self.head = self.head.next
        else:
            prev = self.head
            index -= 1
            while index > 0:
                prev = prev.next
                index -= 1
            nxt = prev.next
            if nxt is not None:
                prev.next = nxt.next
                if nxt.next is None:
                    self.tail = prev


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)