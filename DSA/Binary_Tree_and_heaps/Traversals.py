class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def pre_order_traversal(self, root):
        result = []

        def traversal(node):
            if not node:
                return
            result.append(node.value)
            result.append(node.left)
            result.append(node.right)

        traversal(root)
        return result

    def in_order_traversal(self, root):
        result = []

        def traversal(node):
            if not node:
                return
            result.append(node.left)
            result.append(node.value)
            result.append(node.right)

        traversal(root)
        return result

    def post_order_traversal(self, root):
        result = []

        def traversal(node):
            if not node:
                return
            result.append(node.left)
            result.append(node.right)
            result.append(node.value)

        traversal(root)
        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    # Solution instance
    solution = Solution()

    # Perform postorder traversal
    postorder_result = solution.post_order_traversal(root)
    print("Postorder Traversal:", postorder_result)  # Output: [3, 2, 1]

    # Perform preorder traversal
    preorder_result = solution.pre_order_traversal(root)
    print("Preorder Traversal:", preorder_result)  # Output: [1, 2, 3]

    # Perform inorder traversal
    inorder_result = solution.in_order_traversal(root)
    print("Inorder Traversal:", inorder_result)  # Output: [1, 3, 2]
