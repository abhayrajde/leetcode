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
        
        hm = collections.defaultdict(list)
        
        q = deque([root])
        
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                
                if curr.left:
                    q.append(curr.left)
                    hm[curr].append(curr.left)
                    hm[curr.left].append(curr)
                
                if curr.right:
                    q.append(curr.right)
                    hm[curr].append(curr.right)
                    hm[curr.right].append(curr)
                    
        res = []
        visited = set([target])
        
        q = deque([(target,0)])
        while q:
            for i in range(len(q)):
                curr, moves = q.popleft()
                if moves == k:
                    res.append(curr.val)
                else:
                    for edge in hm[curr]:
                        if(edge not in visited):
                            q.append((edge,moves+1))
                            visited.add(edge)
        return res
        '''
        if not root:
            return []
        res = []
        
        hm = {}
        q = deque([root])
        node = root
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if (curr.val == target.val):
                    node = curr
                    
                if(curr.left):
                    child = curr.left.val
                    parent = [curr]
                    hm[child] = parent
                    q.append(curr.left)
                    
                if(curr.right):
                    child = curr.right.val
                    parent = [curr]
                    hm[child] = parent
                    q.append(curr.right)
                    
        visited = set()
        q = deque([node])
        moves = 0
        while q:
            if(moves == k):
                for i in range(q):
                    curr = q.popleft()
                    res.append(curr.val)
                return
            for i in range(len(q)):
                curr = q.popleft()
                if(curr.left):
                    q.append(curr.left)
                    visited.add(curr.left.val)
                
                if(curr.right):
                    q.append(curr.right)
                    visited.add(curr.right.val)
                
                if(hm[curr.val] not in visited):
                    q.append(hm[curr])
                    visited.add(hm[curr.val].val)
            moves+=1
        '''
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        