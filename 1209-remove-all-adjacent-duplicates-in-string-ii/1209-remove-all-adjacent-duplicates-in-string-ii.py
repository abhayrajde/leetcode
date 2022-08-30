class Solution(object):
    def removeDuplicates(self, s, k):
        stack = []
        for i in range(len(s)):
            if(stack and stack[-1][0] == s[i]):
                stack.append((s[i],stack[-1][1]+1))
                if(stack[-1][1] == k):
                    for j in range(k):
                        stack.pop()
            else:
                stack.append((s[i],1))
        res = ""
        while stack:
            res+=stack.pop()[0]
        return res[::-1]
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        