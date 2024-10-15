"""
Tree Data Structure:

A tree is a hierarchical data structure that consists of nodes connected by edges.

For example:

        A
      / | \
     B  C  D
    /       \
   E         H
  / \
 F   G


Key Terminology:

Node: Each node contains a unique value and may have zero or more child nodes.
      The topmost node of a tree is called the root node (A).
      Nodes with no children are called leaf nodes or terminal nodes (F, G, C and H).

Height: The height of a tree is defined as the number of nodes on the longest path from the root to a leaf node.
"""


class Node:
    """
    A basic node in a tree structure.
    Each node has a value and can have children nodes.
    """

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        raise NotImplementedError()


class Tree:
    """
    A general tree class with methods for adding nodes.
    """

    def __init__(self, root_node_value):
        """
        Initialize an empty tree.
        """
        self.root = Node(root_node_value)

    def get_node(self, value):
        """
        Returns a pointer to the Node object with the corresponding value
        """
        raise NotImplementedError()

    def add_node(self, value, parent):
        """
        Add a node to the tree. Add the node as a child of the parent.

        :param value: The node value.
        :param parent: The parent node value to which the new node should be added as a child.

        :return: a pointer to the node object
        """
        raise NotImplementedError()

    def height(self):
        """
        Returns the height of the tree
        """
        raise NotImplementedError()


class BinaryTree(Tree):
    """
    A tree in which each node has at most two children, known as the left child and the right child.
    This class inheriting from the general tree class.

    You should raise an RuntimeError exception
    """

    def __init__(self, root_node_value):
        super().__init__(root_node_value)

    def set_left_node(self, value, parent):
        """
        Sets a new left node for a given `parent` node value.

        Returns a pointer to the node
        """
        raise NotImplementedError()

    def set_right_node(self, value, parent):
        raise NotImplementedError()


if __name__ == "__main__":
    # Create tree
    #         A
    #       / | \
    #      B  C  D

    t = Tree('A')
    t.add_node('B', parent='A')
    t.add_node('C', parent='A')
    t.add_node('D', parent='A')

    # Create tree
    #         A
    #       / | \
    #      B  C  D
    #     /
    #    E

    t = Tree('A')
    t.add_node('B', parent='A')
    t.add_node('C', parent='A')
    t.add_node('D', parent='A')
    t.add_node('E', parent='B')

    # Create a binary tree
    #         A
    #       /   \
    #      B     C
    #     /     / \
    #    D     E   F
    bt = BinaryTree('A')
    bt.set_left_node('B', parent='A')
    bt.set_right_node('C', parent='A')
    bt.set_left_node('D', parent='B')
    bt.set_left_node('E', parent='C')
    bt.set_right_node('F', parent='C')
    bt.set_right_node('G', parent='C')  # set G as another right node of C should override the existed one, F
    print(bt.height())  # should be 3
