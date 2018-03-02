import unittest


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self, root):
        self.root = root

    def print_tree(self):
        Tree.print_node(self.root)

    def print_node(node):
        Tree._inorder_print(node)
        print('')

    def _inorder_print(node):
        if not node:
            return
        Tree._inorder_print(node.left)
        print(node.value, end=' ')
        Tree._inorder_print(node.right)

    def is_identical(root_a, root_b):
        if root_a is None and root_b is None:
            return True
        if root_a is None or root_b is None:
            return False
        return (root_a.value == root_b.value and
                Tree.is_identical(root_a.left, root_b.left) and
                Tree.is_identical(root_a.right, root_b.right))


class TreeTest(unittest.TestCase):
    def setUp(self):
        self.root_a = Node(6)
        self.root_a.left = Node(4)
        self.root_a.right = Node(7)
        self.root_b = Node(6)
        self.root_b.left = Node(4)
        self.root_b.right = Node(7)
        self.root_b.left.left = Node(2)
        Tree.print_node(self.root_a)

    def test_is_identical(self):
        self.assertTrue(Tree.is_identical(self.root_a, self.root_a))
        self.assertFalse(Tree.is_identical(self.root_a, self.root_b))
        self.assertFalse(Tree.is_identical(self.root_b, self.root_a))

if __name__ == '__main__':
    unittest.main()
