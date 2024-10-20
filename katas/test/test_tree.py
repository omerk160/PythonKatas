import unittest
from katas.tree import Tree, BinaryTree

class TestTree(unittest.TestCase):
    def test_tree_creation(self):
        t = Tree('A')
        t.add_node('B', 'A')  # Removed parent=
        t.add_node('C', 'A')  # Removed parent=
        t.add_node('D', 'A')  # Removed parent=

        self.assertEqual(t.root.value, 'A')
        self.assertEqual(len(t.root.children), 3)

        child_values = [child.value for child in t.root.children]
        self.assertIn('B', child_values)
        self.assertIn('C', child_values)
        self.assertIn('D', child_values)

    def test_tree_height(self):
        t = Tree('A')
        t.add_node('B', 'A')  # Removed parent=
        t.add_node('C', 'A')  # Removed parent=
        t.add_node('D', 'A')  # Removed parent=

        self.assertEqual(t.height(), 2)
        t.add_node('E', 'B')  # Removed parent=
        t.add_node('F', 'E')  # Removed parent=

        self.assertEqual(t.height(), 4)

    def test_binary_tree_creation(self):
        bt = BinaryTree('A')
        bt.set_left_node('B', 'A')  # 'B' is the left child of 'A'
        bt.set_right_node('C', 'A')  # 'C' is the right child of 'A'
        bt.set_left_node('D', 'B')  # 'D' is the left child of 'B'
        bt.set_left_node('E', 'C')  # 'E' is the left child of 'C'
        bt.set_right_node('F', 'C')  # 'F' is the right child of 'C'

        # Assert root node
        self.assertEqual(bt.root.value, 'A')

        # Check children of root node
        self.assertIsNotNone(bt.root.left)  # Left child should exist
        self.assertIsNotNone(bt.root.right)  # Right child should exist
        self.assertEqual(bt.root.left.value, 'B')
        self.assertEqual(bt.root.right.value, 'C')

        # Check children of 'B'
        self.assertIsNotNone(bt.root.left.left)
        self.assertEqual(bt.root.left.left.value, 'D')

        # Check children of 'C'
        self.assertIsNotNone(bt.root.right.left)
        self.assertIsNotNone(bt.root.right.right)
        self.assertEqual(bt.root.right.left.value, 'E')  # Now 'E' should be the left child of 'C'
        self.assertEqual(bt.root.right.right.value, 'F')  # 'F' should be the right child of 'C'

        # Add another right node to 'C', overriding the existing one ('F')
        bt.set_right_node('G', 'C')  # Override right child with 'G'

        self.assertEqual(bt.root.right.right.value, 'G')  # Now 'G' should replace 'F'

    def test_binary_tree_height(self):
        bt = BinaryTree('A')
        bt.set_left_node('B', 'A')  # Removed parent=
        bt.set_right_node('C', 'A')  # Removed parent=
        bt.set_left_node('D', 'B')  # Removed parent=
        bt.set_right_node('E', 'C')  # Removed parent=
        bt.set_left_node('F', 'C')  # Removed parent=

        self.assertEqual(bt.height(), 3)


if __name__ == '__main__':
    unittest.main()
