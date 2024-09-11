from collections import deque
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

firstNode = Node(2)
secondNode = Node(3)
thirdNode = Node(4)
fourthNode = Node(5)

firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode

##Traversals
##DFS
#preorder: root->left->right
def preorder_dfs(node):
    if node is None:
        return
    print(node.data, end=' ')
    preorder_dfs(node.left)
    preorder_dfs(node.right)
#inorder: Left->root->right
def inorder_dfs(node):
    if node is None:
        return 
    inorder_dfs(node.left)
    print(node.data, end=' ')
    inorder_dfs(node.right)
#postorder: left->right->root
def postorder_dfs(node):
    if node is None:
        return
    postorder_dfs(node.left)
    postorder_dfs(node.right)
    print(node.data, end=' ')

##BFS Traversal
def bfs_traversal(node):
    if node is None:
        return
    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.data, end=' ')

        if node.left:
            queue.append(node.left)
            
        if node.right:  
            queue.append(node.right)
