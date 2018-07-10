# coding: utf-8
"""
 栈的特点是「先进后出」
"""


class Node():
    def __init__(self, element=None, next=None):
        self.element = element
        self.next = next

    def __repr__(self):
        return str(self.element)


class Stack():
    def __init__(self):
        self.head = Node()

    def is_empty(self):
        return self.head.next is None

    def push(self, element):
        self.head.next = Node(element, self.head.next)

    def pop(self):
        node = self.head.next
        if not self.is_empty():
            self.head.next = node.next
        return node

    def top(self):
        return self.head.next
