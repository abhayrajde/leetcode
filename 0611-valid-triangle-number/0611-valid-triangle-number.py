class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        res = 0
        for c in range(len(nums)-1,1,-1):
            a = 0
            b = c - 1
            
            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    #WE HAVE A VALID TRIANGLE
                    res += (b - a)
                    b -= 1
                
                else:
                    # we dont have a valid triangle, we want larger values so we move a += 1
                    a += 1
        return res
                    
        """
        :type nums: List[int]
        :rtype: int
        """
        