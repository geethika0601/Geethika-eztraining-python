
# BINARY TREE NODES
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
        
node1=BinaryTreeNode(50)
node2=BinaryTreeNode(20)
node3=BinaryTreeNode(45)
node4=BinaryTreeNode(11)
node5=BinaryTreeNode(15)
node6=BinaryTreeNode(30)
node7=BinaryTreeNode(78)

node1.leftchild=node2
node1.rightchild=node3
node2.leftchild=node4
node2.rightchild=node5
node3.leftchild=node6
node3.rightchild=node7

print("root node is:")
print(node1.data)

print("right child of the node is:")
print(node1.leftchild.data)

print("root node is :")
print(node2.data)

print("left child of the node is:")
print(node2.leftchild.data)

print("right child of the node is:")
print(node2.rightchild.data)




#
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val,end=" ")
        printInorder(root.right)
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val,end=" ")
def printPreorder(root):
    if root:
        print(root.val,end=" ")
        printPreorder(root.left)
        printPreorder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("\n Preorder:")
printPreorder(root)
print()
print("\n Inorder:")
printInorder(root)
print()
print("\n Postorder:")
printPostorder(root)
print()


#BST INSERTION
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
        return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r=Node(50)
r=insert(r,30)
r=insert(r,20)
r=insert(r,40)
r=insert(r,70)
r=insert(r,60)
r=insert(r,80)
inorder(r)

#

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node

def minValueNode(node):
    current=node
    while(current.left is not None):
        current=current.left
    return current
def deleteNode(root,key):
    if root is None:
        return root
    if key<root.key:
        root.left=deleteNode(root.left,key)
    else(key>root.key):
        root.right=deleteNode(root.right,key)
