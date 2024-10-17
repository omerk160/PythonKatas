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
        bt.set_left_node('B', 'A')  # Removed parent=
        bt.set_right_node('C', 'A')  # Removed parent=
        bt.set_left_node('D', 'B')  # Removed parent=
        bt.set_right_node('E', 'C')  # Removed parent=
        bt.set_left_node('F', 'C')  # Removed parent=

        self.assertEqual(bt.root.value, 'A')
        self.assertEqual(len(bt.root.children), 2)

        self.assertIn('B', [c.value for c in bt.root.children])
        self.assertIn('C', [c.value for c in bt.root.children])

        for c in bt.root.children:
            if c.value == 'B':
                self.assertEqual(len(c.children), 1)
                self.assertEqual(c.children[0].value, 'D')
            elif c.value == 'C':
                self.assertEqual(len(c.children), 2)
                self.assertIn('E', [c2.value for c2 in c.children])
                self.assertIn('F', [c2.value for c2 in c.children])

        # Add another right node to 'C', overriding the existing one ('E')
        bt.set_right_node('G', 'C')  # Removed parent=

        for c in bt.root.children:
            if c.value == 'C':
                self.assertEqual(len(c.children), 2)
                self.assertIn('G', [c2.value for c2 in c.children])
                self.assertIn('F', [c2.value for c2 in c.children])

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
