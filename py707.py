class ListNode:
    def __init(self, val, next=None) -> None:
        self.val = val 
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1 
        
        cur = self.dummy_head.next # 此处需要有具体的value，所以是从dummy next开始
        for _ in range(index):
            cur = cur.next 
        else:
            return cur.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:        
        cur = self.dummy_head
        while cur.next:
            cur = cur.next 
        else:
            cur.next = ListNode(val=val, next=None)
        
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size: 
            return        
        
        cur = self.dummy_head
        
        for _ in range(index):  
            cur = cur.next 
        else:
            cur.next = ListNode(val, cur.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        cur = self.dummy_head

        for _ in range(index):
            cur = cur.next 
        else:
            cur.next = cur.next.next 

        self.size -= 1
if __name__ == "__main__":
# Your MyLinkedList object will be instantiated and called as such:
    pass