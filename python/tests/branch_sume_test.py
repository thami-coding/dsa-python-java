# Add, edit, or remove tests in this file.
# Treat it as your playground!


import unittest
from algo_expert.branch_sum import branchSums, BinaryTree
from collections import deque


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(1)
        self.assertEqual(branchSums(tree), [1])

    def test_case_2(self):
        tree = BinaryTree(1).insert([2])
        self.assertEqual(branchSums(tree), [3])

    def test_case_3(self):
        tree = BinaryTree(1).insert([2, 3])
        self.assertEqual(branchSums(tree), [3, 4])

    def test_case_4(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5])
        self.assertEqual(branchSums(tree), [7, 8, 4])

    def test_case_5(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(branchSums(tree), [15, 16, 18, 10, 11])

    def test_case_6(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1])
        self.assertEqual(branchSums(tree), [15, 16, 18, 9, 11, 11, 11])

    def test_case_7(self):
        tree = BinaryTree(0)
        tree.left = BinaryTree(1)
        tree.left.left = BinaryTree(10)
        tree.left.left.left = BinaryTree(100)
        self.assertEqual(branchSums(tree), [111])

    def test_case_8(self):
        tree = BinaryTree(0)
        tree.right = BinaryTree(1)
        tree.right.right = BinaryTree(10)
        tree.right.right.right = BinaryTree(100)
        self.assertEqual(branchSums(tree), [111])

    def test_case_9(self):
        tree = BinaryTree(0)
        tree.left = BinaryTree(9)
        tree.right = BinaryTree(1)
        tree.right.left = BinaryTree(15)
        tree.right.right = BinaryTree(10)
        tree.right.right.left = BinaryTree(100)
        tree.right.right.right = BinaryTree(200)
        self.assertEqual(branchSums(tree), [9, 16, 111, 211])



class BinaryTree(BinaryTree):

    def insert(self, values):
        """Insert a list of values into the tree in level-order fashion."""
        queue = deque([self])

        for v in values:
            while queue:
                current = queue[0]  # Look at the first element in queue
                if current.left is None:
                    current.left = BinaryTree(v)
                    queue.append(current.left)
                    break
                elif current.right is None:
                    current.right = BinaryTree(v)
                    queue.append(current.right)
                    break
                else:
                    queue.popleft()  # Both children occupied, move on

        return self


if __name__ == "__main__":
    unittest.main()
