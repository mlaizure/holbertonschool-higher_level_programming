#!/usr/bin/python3
"""Module makes a node for a linked list and creates a sorted list"""


class Node:
    """Class with data and next_node attributes"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves data value"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets value of data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Class with head attribute and sorted insert method"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list"""
        if self.__head is None:
            self.__head = Node(value, None)
        elif value < self.__head.data:
            self.__head = Node(value, self.__head)
        else:
            n = self.__head
            while n.next_node is not None and n.next_node.data <= value:
                n = n.next_node
            new_node = Node(value, n.next_node)
            n.next_node = new_node

    def __str__(self):
        n = self.__head
        str = ""
        while n is not None:
            str += "{}\n".format(n.data)
            n = n.next_node
        return str[:-1]
