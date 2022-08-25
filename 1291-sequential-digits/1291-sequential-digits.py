class Solution(object):
    def sequentialDigits(self, low, high):
        digits = "123456789"
        l = len(str(low))
        h = len(str(high))
        res = []
        
        for i in range(l,h+1):
            for j in range(0,10-i):
                nums = int(digits[j:j+i])
                if((int(nums) >= low and int(nums)<=high)):
                    res.append(nums)
        return res
        
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        