class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=None

    def get(self, index: int) -> int:
        temp=self.head
        for i in range(index):
            if temp is None:
                return -1
            temp=temp.next
        if temp:
            return temp.data
        return -1

    def addAtHead(self, val: int) -> None:
        new=Node(val)
        new.next=self.head
        self.head=new

    def addAtTail(self, val: int) -> None:
        if self.head==None:
            self.addAtHead(val)
        else:
            new=Node(val)
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
            return

        new=Node(val)
        temp=self.head

        for i in range(index-1):
            if temp is None:
                return
            temp=temp.next

        if temp is None:
            return

        new.next=temp.next
        temp.next=new

    def deleteAtIndex(self, index: int) -> None:
        if self.head:
            if index==0:
                self.head=self.head.next
            else:
                temp=self.head
                for i in range(index-1):
                    if temp.next is None:
                        return
                    temp=temp.next

                if temp.next:
                    temp.next=temp.next.next