# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        if not k:
            return [target.val]
        
        hm = defaultdict(list)
        
        q = deque([root])
        
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                
                if curr.left:
                    q.append(curr.left)
                    hm[curr.left].append(curr)
                    hm[curr].append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
                    hm[curr.right].append(curr)
                    hm[curr].append(curr.right)
                    
                    
        res = []
        q = deque([(target,0)])
        visited = set([target])
        while q:
            for i in range(len(q)):
                curr, moves = q.popleft()
                if moves == k:
                    res.append(curr.val)
                else:
                    for edge in hm[curr]:
                        if edge not in visited:
                            q.append((edge,moves+1))
                            visited.add(edge)
        return res
        
        
        
#         # T.C - O(N) + O(N) => O(2N) => O(N)
#         # S.C - O(N) + O(N) => O(2N) => O(N)
#         if not k:
#             return [target.val]
        
#         hm = collections.defaultdict(list)
        
#         q = deque([root])
        
#         while q:                    #O(N)
#             for i in range(len(q)):
#                 curr = q.popleft()
                
#                 if curr.left:
#                     q.append(curr.left)
#                     hm[curr].append(curr.left)
#                     hm[curr.left].append(curr)
                
#                 if curr.right:
#                     q.append(curr.right)
#                     hm[curr].append(curr.right)
#                     hm[curr.right].append(curr)
                    
#         res = []
#         visited = set([target])
        
#         q = deque([(target,0)])
#         while q:
#             for i in range(len(q)):
#                 curr, moves = q.popleft()
#                 if moves == k:
#                     res.append(curr.val)
#                 else:
#                     for edge in hm[curr]:
#                         if(edge not in visited):
#                             q.append((edge,moves+1))
#                             visited.add(edge)
#         return res
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        