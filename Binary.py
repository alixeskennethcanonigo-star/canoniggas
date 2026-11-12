class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Constructing the Binary Tree based on last name: CANONIGO
# Level 0: C
root = Node("C")

# Level 1: A, N
root.left = Node("A")
root.right = Node("N")

# Level 2: O, N, I, G
root.left.left = Node("O")
root.left.right = Node("N")
root.right.left = Node("I")
root.right.right = Node("G")

# Level 3: O (child of G)
root.right.right.right = Node("O")


# Breadth-First Search (BFS / Level Order) Algorithm
def bfs_binary_tree(root_node):
    if not root_node:
        return
    queue = [root_node]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current.data)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    print("Binary Tree BFS Result:", " - ".join(result))


# Depth-First Search (DFS / Preorder: Root, Left, Right) Algorithm
def dfs_binary_tree(root_node, result=None):
    if result is None:
        result = []
    if root_node:
        result.append(root_node.data)
        dfs_binary_tree(root_node.left, result)
        dfs_binary_tree(root_node.right, result)
    return result


if __name__ == "__main__":
    print("--- BINARY TREE TRAVERSAL (CANONIGO) ---")
    bfs_binary_tree(root)

    dfs_result = dfs_binary_tree(root)
    print("Binary Tree DFS Result:", " - ".join(dfs_result))