#!/usr/bin/python3

"""
Module Name: singly_linked_list

This module defines two classes, Node and SinglyLinkedList.

Classes:
    Node: Represents a node in a linked list.
    SinglyLinkedList: represents a singly linked list.

Usage:
    sll = SinglyLinkedList() # creates a new linked list
    sll.sorted_insert(n) # inserts a node with value n in the linked list
    print(sll) # prints the linked list.
"""


class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The next node in the linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Args:
            data (int): The data.
            next_node (Node, optional): The next node.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Gets the data stored in the node.

        Returns:
            int: The stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Stores the value in the node

        Args:
            value (int): The new data value for the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Gets the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Args:
            value (Node): The new next node in the linked list.

        Raises:
            TypeError: If value is not a Node.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represent a sigly linked list

    Attributes:
        __head (Node): The head of the linked list.
    """
    def __init__(self):
        """ Initializes a new instance of the SinglyLinkedList class """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node with a sorted value into the linked list.

        Args:
            value (int): The value to be inserted into the linked list.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """
        Returns a representation of the linked list.

        Returns:
            str: A string representing the linked list.
        """
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
