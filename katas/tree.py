class Node:
    """
    A basic node in a tree structure.
    Each node has a value and can have children nodes.
    """

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        """Add a child node."""
        self.children.append(child)


class Tree:
    """
    A general tree class with methods for adding nodes.
    """

    def __init__(self, root_node_value):
        """
        Initialize a tree with a root node.
        """
        self.root = Node(root_node_value)

    def get_node(self, value, node=None):
        """
        Returns a pointer to the Node object with the corresponding value.
        """
        if node is None:
            node = self.root

        if node.value == value:
            return node

        for child in node.children:
            result = self.get_node(value, child)
            if result is not None:
                return result
        return None

    def add_node(self, value, parent_value):
        """
        Add a node to the tree as a child of the specified parent.

        :param value: The node value.
        :param parent_value: The parent node value to which the new node should be added as a child.
        :return: a pointer to the newly added node object.
        """
        parent_node = self.get_node(parent_value)
        if parent_node is None:
            raise RuntimeError(f"Parent node {parent_value} not found.")

        new_node = Node(value)
        parent_node.add_child(new_node)
        return new_node

    def height(self, node=None):
        """
        Returns the height of the tree.
        """
        if node is None:
            node = self.root

        if not node.children:  # If there are no children, it's a leaf node.
            return 1

        heights = [self.height(child) for child in node.children]
        return 1 + max(heights)


class BinaryTree(Tree):
    """
    A binary tree in which each node has at most two children (left and right).
    """

    def __init__(self, root_node_value):
        super().__init__(root_node_value)

    def set_left_node(self, value, parent_value):
        """
        Sets a new left node for a given parent node value.
        Returns a pointer to the newly added node.
        """
        parent_node = self.get_node(parent_value)
        if parent_node is None:
            raise RuntimeError(f"Parent node {parent_value} not found.")

        if len(parent_node.children) > 0:
            # If left child already exists, override it
            parent_node.children[0] = Node(value)  # Replace left child
        else:
            parent_node.add_child(Node(value))

        return parent_node.children[0]

    def set_right_node(self, value, parent_value):
        """
        Sets a new right node for a given parent node value.
        Returns a pointer to the newly added node.
        """
        parent_node = self.get_node(parent_value)
        if parent_node is None:
            raise RuntimeError(f"Parent node {parent_value} not found.")

        if len(parent_node.children) > 1:
            # If right child already exists, override it
            parent_node.children[1] = Node(value)  # Replace right child
        else:
            parent_node.add_child(Node(value))

        return parent_node.children[-1]  # Return the rightmost child


if __name__ == "__main__":
    # Create tree
    #         A
    #       / | \
    #      B  C  D

    t = Tree('A')
    t.add_node('B', 'A')  # Change to 'B', 'A' (removed keyword)
    t.add_node('C', 'A')  # Change to 'C', 'A' (removed keyword)
    t.add_node('D', 'A')  # Change to 'D', 'A' (removed keyword)

    # Create tree
    #         A
    #       / | \
    #      B  C  D
    #     /
    #    E

    t.add_node('E', 'B')  # Change to 'E', 'B' (removed keyword)

    # Create a binary tree
    #         A
    #       /   \
    #      B     C
    #     /     / \
    #    D     E   F
    bt = BinaryTree('A')
    bt.set_left_node('B', 'A')  # Change to 'B', 'A' (removed keyword)
    bt.set_right_node('C', 'A')  # Change to 'C', 'A' (removed keyword)
    bt.set_left_node('D', 'B')  # Change to 'D', 'B' (removed keyword)
    bt.set_left_node('E', 'C')  # Change to 'E', 'C' (removed keyword)
    bt.set_right_node('F', 'C')  # Change to 'F', 'C' (removed keyword)
    bt.set_right_node('G', 'C')  # Override right child with G
    print(bt.height())  # Output should be 3
