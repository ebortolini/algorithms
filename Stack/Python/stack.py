#based on: https://algs4.cs.princeton.edu/13stacks/Stack.java.html

from typing import TypeVar, Generic, Union

Item = TypeVar("Item")

class Node(Generic[Item]):
    def __init__(self, item:Item) -> None:
        self.item = item
        self.next: Node|None = None

class Stack(Generic[Item]):
    def __init__(self) -> None:
        self.first: Node|None = None
        self.size: int = 0
    
    def isEmpty(self) -> bool:
        return self.first is None
    
    def push(self, item:Item) -> None:
        node = Node[Item](item)
        node.next = self.first
        self.first = node
        self.size+=1
    
    def pop(self) -> Item:
        if self.first is None:
            raise IndexError("Stack is empty")
        node = self.first
        self.first = self.first.next
        self.size-=1
        return node.item