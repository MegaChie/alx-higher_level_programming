#!/usr/bin/python3
""" python singly linked list """


class Node:
    """ Singly linked list
    args: data - value of node
          next_node - pointer to next node in list """
    def __init__(self, data, next_node=None)
        self.data = data
        self.next_node = next_node

    """ Singly linked list """
    def data(self):
        return (self.__data)

    """ Singly linked list
    args: value - value of to put in node's data """
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    """ Singly linked list """
    def next_node(self):
        return (self.__next_node)

    """ Singly linked list
    args: value - value of to put in node's data """
    def next_node(self, value):
        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """ defines a singly linked list """

    """ Singly linked list """
    def __init__(self):
        self.head = None

    """ Singly linked list """
    def __str__(self):
        printsll = ""
        location = self.head
        while location:
            printsll += str(location.data) + "\n"
            location = location.next_node
        return printsll[:-1]

    """ Singly linked list
    args: value - value of to put in node's data """
    def sorted_insert(self, value):
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new
