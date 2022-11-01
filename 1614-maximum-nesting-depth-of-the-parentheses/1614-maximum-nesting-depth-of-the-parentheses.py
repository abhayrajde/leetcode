class Solution(object):
    def maxDepth(self, s):
        stack = []
        maxcnt = 0
        for i in s:
            if i == "(":
                if stack:
                    stack.append(stack[-1]+1)
                else:
                    stack.append(1)
                maxcnt = max(maxcnt,stack[-1])
            elif i == ")":
                stack.pop()
        
        return maxcnt
        """
        :type s: str
        :rtype: int
        """
        