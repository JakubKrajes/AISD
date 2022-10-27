
from typing import Any

class Node:
    value: Any
    next: 'Node'
    def __init__(self, value: Any)->None:
        self.value=value

class LinkedList:
    head: Node
    tail: Node
    def __init__(self)->None:
        self.head = None
        self.tail = None
        
    def push(self,element: Any)->None:
        node = Node(element)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.tail
            self.head = node

    def append(self,element):
        lastnode = Node(element)
        lastnode.next = None
        self.tail = lastnode

    def len(self):
        node=self.head
        len=0

        while node is not None:
            len=len+1
            node=node.next
        return len

    def remove_last(self):
        element = self.tai
         i=0

        while(i<after):
            currentNode=currentNode.next
            i=i+1

        currentNode.next=currentNode.next.next
  
    def print(self)->None:
        node=self.head

        while node is not None:
            print(node.value,"-> ", end="")
            node=node.next
        print("None")
list_=LinkedList()
list_.append(3)
list_.append(4)
list_.push(5)
#print(list_.NodePos(0))
list_.print()
list_.insertNode(8,1)
list_.print()
print(list_.pop())
print(list_.removeLast())
list_.print()
list_.append(6)
list_.append(10)
list_.print()
list_.remove(1)
list_.print()
print(list_.len())
