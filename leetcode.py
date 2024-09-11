class Node:
    def __init__(self, node):
        self.data = node
        self.left = None
        self.right = None

    def inorderTraversal(self,node):
        result = []
        self._inorder(node, result)
        return result
    
    def _inorder(self,node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.data)
        self._inorder(node.right, result)

firstNode = Node(2)
secondNode = Node(3)
thirdNode = Node(4)
fourthNode = Node(5)
firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode

solution = Node(0)  # Creating a dummy node just to call the method
print(solution.inorderTraversal(firstNode))