#!/usr/bin/python3
"""class that implement a singly linked list"""


class Node:
    """class that defines a node of a singly linked list
    Attributes:
        data (int): data
        next_node (None or Node): link to item in the list
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class defines the singly linked list
    Attributes:
        head:
    """
    def __init__(self):
        self.__head = None

    def __str__(self):
        if self.__head is None:
            return ""

        string = ""
        current_node = self.__head
        while current_node:
            string += str(current_node.data) + "\n"
            current_node = current_node.next_node
        return string.rstrip('\n')

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node and value > current.next_node.data:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
