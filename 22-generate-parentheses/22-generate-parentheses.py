class Solution(object):
    def generateParenthesis(self, n):
        # only add open parenthesis if open < n
        # only add closed parenthesis if closed < open
        # only return the string as valid iff open == closed == n 
        
        stack = []
        res = []
        
        def validback(openN, closeN):
            if(openN == closeN == n):
                temp = ""
                for i in stack:
                    temp+=i
                res.append(temp)
                return
            
            if(openN < n):
                stack.append("(")
                validback(openN+1,closeN)
                stack.pop()
            
            if(closeN < openN):
                stack.append(")")
                validback(openN, closeN+1)
                stack.pop()
        
        validback(0,0)
        return(res)
            
        
        """
        :type n: int
        :rtype: List[str]
        """
        