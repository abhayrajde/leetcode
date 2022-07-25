class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []    # pair: [temp,index]
        
        for ind, temp in enumerate(temperatures):
            while(stack and (temp > stack[-1][0])):
                stackT, stackInd = stack.pop()
                res[stackInd] = ind - stackInd
            stack.append([temp, ind])
        return res
        
        
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        