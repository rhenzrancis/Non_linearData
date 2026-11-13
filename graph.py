"""
Assessment 3.4 - Program for Diagram 1: Binary Tree
Last name: MABIDA

Builds a binary search tree from the letters of the last name
(smaller or equal letters go left, larger letters go right),
then prints the BFS and DFS traversals.
"""

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    """Insert a value into the BST. Duplicates go to the left."""
    if root is None:
        return Node(value)
    if value <= root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def bfs(root):
    """Breadth-First Search (level order) using a queue."""
    result = []
    if root is None:
        return result
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def preorder(node, result):
    """DFS: Root -> Left -> Right"""
    if node:
        result.append(node.value)
        preorder(node.left, result)
        preorder(node.right, result)
    return result


def inorder(node, result):
    """DFS: Left -> Root -> Right"""
    if node:
        inorder(node.left, result)
        result.append(node.value)
        inorder(node.right, result)
    return result


def postorder(node, result):
    """DFS: Left -> Right -> Root"""
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.value)
    return result


def print_tree(node, level=0, label="root"):
    """Print the tree sideways so its shape is visible in the console."""
    if node:
        print_tree(node.right, level + 1, "R")
        print("    " * level + f"{label}: {node.value}")
        print_tree(node.left, level + 1, "L")


if __name__ == "__main__":
    last_name = "MABIDA"

    root = None
    for letter in last_name:
        root = insert(root, letter)

    print("Binary tree for", last_name)
    print_tree(root)

    print("\nBFS (level order):", " -> ".join(bfs(root)))
    print("DFS pre-order    :", " -> ".join(preorder(root, [])))
    print("DFS in-order     :", " -> ".join(inorder(root, [])))
    print("DFS post-order   :", " -> ".join(postorder(root, [])))