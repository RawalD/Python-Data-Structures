"""
Branch: Path at the top of the binary tree
Leaf nodes: Last elements in that node

Our binary tree
          1
         /  \
        2    3
       /\    /\
      4  5   6 7
     /\   \
    8  9  10

Result = [15,16,18,10,11]
1 + 2 + 4 + 8 = 15
1 + 2 + 4 + 9 = 16
1 + 2 + 5 + 10 = 18
1 + 3 + 6 = 10
1 + 3 + 7 = 11

Running sum = 0 , we have done no calculations yet and this is the basis of the node 
Running sum = 0 + 1 , this is when we go to 2 and 3 children nodes
Running sum for 2 = 1 + 2, Running sum for 3 = 1 + 3
Running sum on 4 is 3, right child is 3
Running sum on 6 is 4, right child is 4
Running sum on 8 is 4+3 = 7, right child is same
Running sum on 10 is 1 + 3 + 5, right child is the same

Still confusing and needs to be paid more attention
"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sum(root):
    # Sum list
    sums = []

    # Running sum is currently 0
    calc_branch_sum(root, 0, sums)

    return sums


def calc_branch_sum(node, running_sum, sums):

    if node is None:
        return

    new_running_sum = running_sum + node.value

    if node.left is None and node.right is None:
        sums.append(new_running_sum)

        return

    calc_branch_sum(node.left, new_running_sum, sums)
    calc_branch_sum(node.right, new_running_sum, sums)


tree = BinaryTree(1)
print(branch_sum(tree))
