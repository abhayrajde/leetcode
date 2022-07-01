class Solution(object):
    def canJump(self, nums):
        goal = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if((nums[i]+i)>=goal):
                goal = i
        if(goal == 0):
            return(True)
        else:
            return(False)
        
        """reach = [False]*len(nums)
        # reach[-1] = True
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]+i >= len(nums)-1):
                reach[i] = True
            else:
                for j in range(i,nums[i]+i+1):
                    if(reach[j]):
                        reach[i] = True
                        break
        return(reach[0])
        """
        """
        :type nums: List[int]
        :rtype: bool
        """
        