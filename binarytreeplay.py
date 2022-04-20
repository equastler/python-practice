class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)
node0.left = node1
node0.right = node2
tree = node0
print(tree.right.key)

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data == None:
        node = None
    else:
        node = TreeNode(data)
    return node
#converts tuple style notation to objects in class TreeNode (tree nodes) in binary tree structure
testnode = parse_tuple((1,2,3))
print(testnode.left.key)

#traversals of binary trees

def traverse_in_order(node):
    if node == None:
        return []
    return (traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right))

print(traverse_in_order(testnode))
#see preorder and postorder traversals also
#basically every operation with trees involves recursion, as we are seeing

def tree_height(node):
    if node == None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

#think of the whole tree represented by the root node

print(tree_height(testnode))

def tree_size(node):
    if node == None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)
print(tree_size(testnode))
