import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

N = int(input())

def preorder_traverse(node):
    print(node.data, end='')

    if node.left_node != '.':
        preorder_traverse(tree[node.left_node])

    if node.right_node != '.':
        preorder_traverse(tree[node.right_node])

def inorder_traverse(node):

    if node.left_node != '.':
        inorder_traverse(tree[node.left_node])

    print(node.data, end='')

    if node.right_node != '.':
        inorder_traverse(tree[node.right_node])

def postorder_traverse(node):
    if node.left_node != '.':
        postorder_traverse(tree[node.left_node])

    if node.right_node != '.':
        postorder_traverse(tree[node.right_node])

    print(node.data, end='')

tree = {}
for _ in range(N):
    data, left_node, right_node = input().split()
    tree[data] = Node(data, left_node, right_node)
    

preorder_traverse(tree["A"])
print()
inorder_traverse(tree["A"])
print()
postorder_traverse(tree["A"])