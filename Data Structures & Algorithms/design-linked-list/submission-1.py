class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)  # sentinel
        self.tail = ListNode(0)  # sentinel
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def getPrev(self, index: int) -> ListNode:
        """Returns the node at position index-1 (the predecessor)."""
        if index <= self.size // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail
            for _ in range(self.size - index + 1):
                cur = cur.prev
        return cur

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self.getPrev(index).next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        node = ListNode(val)
        prev = self.getPrev(index)
        nxt = prev.next

        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        prev = self.getPrev(index)
        cur = prev.next
        nxt = cur.next

        prev.next = nxt
        nxt.prev = prev

        self.size -= 1