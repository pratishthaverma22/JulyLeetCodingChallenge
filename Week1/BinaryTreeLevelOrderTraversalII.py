/*
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
*/


class Solution:
    def levelOrderBottom(self, root):
        if not root: return []
    
        Out_temp, deq = [], deque([[root, 0]])
    
        while deq:
            elem = deq.popleft()
            Out_temp.append([elem[0].val, elem[1]])
            if elem[0].left:
                deq.append([elem[0].left, elem[1] + 1])
            if elem[0].right:
                deq.append([elem[0].right, elem[1] + 1])

        Out = [[Out_temp[0][0]]]
        for i in range(1, len(Out_temp)):
            if Out_temp[i][1] == Out_temp[i-1][1]:
                Out[Out_temp[i][1]].append(Out_temp[i][0])
            else:
                Out.append([Out_temp[i][0]])

        return Out[::-1]
