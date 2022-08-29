class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for num in asteroids:
            if(num > 0):
                stack.append(num)
            else:
                
                # If the num is negative - 3 possible scenarios
                # 1. the top element in stack is small then neg num
                while stack and stack[-1] > 0 and stack[-1] < abs(num):
                    stack.pop()
                
                #2. the stack is empy or the top element already in stack is negative
                if(not stack or stack[-1] < 0):
                    stack.append(num)
                
                #3. both the neg num and the top element of the stack are equal
                elif stack[-1] == -num:
                    stack.pop()
        return stack      
            
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        