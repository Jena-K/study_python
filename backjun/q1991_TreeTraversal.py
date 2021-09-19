'''
import sys
sys.setrecursionlimit(10**6)

tree = {}
n = int(input())
for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)


def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')

'''
import sys
sys.setrecursionlimit(10**6)

tree = {}
n = int(input())
for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)
result = ['','','']

def TreeTraversal(node):
    if node == '.':
        return
    result[0] += node
    TreeTraversal(tree[node][0])
    result[1] += node
    TreeTraversal(tree[node][1])
    result[2] += node


TreeTraversal('A')
for i in result:
    print(i)
