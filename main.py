# Binary Tree
# DFS(Depth First Seach) => inorder,proeorder,postorder
# BFS(Breadth First Search) => queue
# Inorder => (left->node->right)
# Preorder => (node->left->right)
# Postorder => (left->right->node)

class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(2)
D = TreeNode(3)
E = TreeNode(4)
F = TreeNode(4)
G = TreeNode(3)
#       1
#    2      3
#  4   5  10

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G

# inorder => left->node->right
# 4,2,5,1,10,3
def in_order(node:TreeNode):
    if not node:return
    left = in_order(node.left)
    print(node.val)
    right = in_order(node.right)
    
# print(in_order(A))

# pre_order => node->left->right
# 1,2,4,5,3,10
def pre_order(node:TreeNode):
    if not node:return
    print(node.val)
    left = pre_order(node.left)
    right = pre_order(node.right)
    
# print(pre_order(A))

# post_order => left->right->node
# 4,5,2,10,3,1
def post_order(node:TreeNode):
    if not node:return 
    left = post_order(node.left)
    right = post_order(node.right)
    print(node.val)
    
print(post_order(A))

# preoder_itermethod 
# 1,2,4,5,3,10
def pre_order_iter(node:TreeNode):
    stack = [node]
    while stack:
        node = stack.pop()
        if node.right: stack.append(node.right)
        print(node.val)
        if node.left: stack.append(node.left)
    
# pre_order_iter(A)

# inorder_iter
# 4,2,5,1,10,3
def in_order_iter(node:TreeNode):
    stack = []
    curr = node
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print(curr.val)
        curr = curr.right
        
# in_order_iter(A)

# post_order_iter
# 4,5,2,10,3,1
def post_order_iter(node: TreeNode):
    if not node:
        return

    s1 = [node]
    s2 = []

    while s1:
        curr = s1.pop()
        s2.append(curr)

        if curr.left:
            s1.append(curr.left)
        if curr.right:
            s1.append(curr.right)

    while s2:
        print(s2.pop().val)
        
# post_order_iter(A)

def search(node:TreeNode,target):
    if not node:return False
    if node.val == target:return True
    return search(node.left,target) or search(node.right,target)

# print(search(A,12))
        
# preorder
# 1,2,4,5,3,10
# node - left - right
def preorder(node:TreeNode):
    if not node: return
    stack = [node]
    ans = []
    while stack:
        curr = stack.pop()
        ans.append(curr.val)
        if curr.right: stack.append(curr.right)
        if curr.left: stack.append(curr.left)
    return ans

print(preorder(A))


# inorder_iter
# 4,2,5,1,10,3
# left->node->right
def inorder(node:TreeNode):
    stack = []
    ans = []
    curr = node
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        ans.append(curr.val)
        curr = curr.right
    return ans
        
print(inorder(A))

# postorder iter
# 4,5,2,10,3,1
# left-right-node
def postorderiter(node:TreeNode):
    if not node: return
    stack1 = [node]
    stack2 = []
    
    while stack1:
        curr = stack1.pop()
        stack2.append(curr.val)
        if curr.left : stack1.append(curr.left)
        if curr.right : stack1.append(curr.right)
    return list(reversed(stack2))

print(postorderiter(A),"------")


# postorder iter
# 4,5,2,10,3,1
# left-right-node

def postorderstack(node:TreeNode):
    if not node: return
    stack = []
    ans = []
    curr = node
    last_visited = None
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        peek_node = stack[-1]
        if peek_node.right and peek_node.right!=last_visited:
            curr = peek_node.right
        else:
            ans.append(peek_node.val)
            last_visited = stack.pop()
    return ans
print(postorderstack(A),"=======")


# BFS
# =========
#       1
#    2      3
#  4   5  10
# output => [[1],[2,3],[4,5,10]]
def bfs_travesal(node:TreeNode):
    if not node: return
    que = [node]
    ans = []
    
    while que:
        lev_arr = []
        lev_size = len(que)
        for i in range(lev_size):
            cur = que.pop(0)
            lev_arr.append(cur.val)
            if cur.left : que.append(cur.left)
            if cur.right : que.append(cur.right)
        ans.append(lev_arr)
        # ans.reverse()
    return ans
        

print(bfs_travesal(A),"proroororor")

    
# BFS
# =========
#       1
#    2      3
#  4   5  10
# zigzag => [[1],[3,2],[4,5,10]]

def bfs_zigzag_travesal(node:TreeNode):
    if not node: return []
    que = [node]
    ans = []
    level = 0
    while que:
        level_size = len(que)
        level_array = []
        for i in range(level_size):
            curr = que.pop(0)
            level_array.append(curr.val)
            if curr.left: que.append(curr.left)
            if curr.right: que.append(curr.right)
        if level%2==1:
            level_array.reverse()
        ans.append(level_array)
        level += 1
            
    return ans

print(bfs_zigzag_travesal(A))


# recursion
def ok():
    ans = []
    def rec(node:TreeNode,level:int):
        if level == len(ans):
            ans.append([])
        ans[level].append(node.val)
        if node.left: rec(node.left,level=level+1)
        if node.right: rec(node.right,level=level+1)
        return ans
    rec(A,0)
    return ans

print(ok())
    

# Max_depth of a binary tree
# top-down approach
def max_dept(node:TreeNode):
    max_depth = 0
    curr = node
    def traverse(curr,depth):
        max_dept = max(max_dept,depth)
        if curr.left: traverse(curr.left,depth=depth+1)
        if curr.right: traverse(curr.right,depth=depth+1)
        
    traverse(curr,max_depth)
    return max_depth


# max depth
# bottom up approach
def max_depth_b(node:TreeNode):
    if not node: return 0
    left_max = max_depth_b(node.left)
    right_max = max_depth_b(node.right)
    return 1 + max(left_max,right_max) 

def symmetric_tree_recursion(node:TreeNode):
    def isSymmetric(left,right):
        if not left and not right: return True
        if not left or not right: return False
        return left.val == right.val and isSymmetric(left.right,right.left) and isSymmetric(left.left,right.right)
    return isSymmetric(node.left,node.right)

print(symmetric_tree_recursion(A))


def symmetric_tree_loop(node:TreeNode):
    que = [node.left,node.right]
    while que:
        p1 = que.pop(0)
        p2 = que.pop(0)
        
        if not p1 or not p2: continue
        if p1.val != p2.val: return False
        
        que.extend([p1.left,p2.right])
        que.extend([p1.right,p2.left])
    return True

print(symmetric_tree_loop(A))