# coding: utf-8
"""
队列的特点是「先进先出」
"""


class Node():
    def __init__(self, element=None, next=None):
        self.element = element
        self.next = next

    def __repr__(self):
        return str(self.element)


class Queue():
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def empty(self):
        return self.head.next is None

    def enqueue(self, element):
        n = Node(element)
        self.tail.next = n
        self.tail = n

    def dequeue(self):
        node = self.head.next
        if not self.empty():
            self.head.next = node.next
        return node
