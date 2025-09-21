from collections import deque


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values):
        queue = deque([self])

        for v in values:
            while queue:
                current = queue[0]

                if current.left is None:
                    current.left = BinaryTree(v)
                    queue.append(current.left)
                    break
                elif current.right is None:
                    current.right = BinaryTree(v)
                    queue.append(current.right)
                    break
                else:
                    queue.popleft()
        return self


def branchSums(root):
    sums = []
    calculateTotalSums(root, 0, sums)
    return sums


def calculateTotalSums(node, runningSum, sums):
    if node is None:
        return
    newRunningSums = node.value + runningSum
    if node.left is None and node.right is None:
        sums.append(newRunningSums)
        return

    calculateTotalSums(node.left, newRunningSums, sums)
    calculateTotalSums(node.right, newRunningSums, sums)
