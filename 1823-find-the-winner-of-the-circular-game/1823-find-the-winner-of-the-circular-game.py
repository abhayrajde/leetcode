class Solution(object):
    def findTheWinner(self, n, k):
        stack1 = [i for i in range(1,n+1)]
        stack2 = []
        while((len(stack1) + len(stack2)) > 1):
            for i in range(k):
                if i == k-1:
                    stack1.pop(0)
                else:
                    stack2.append(stack1.pop(0))
                if not stack1:
                    stack1,stack2 = stack2,stack1
                
        return stack1[0]

                
                
        
        
        
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        