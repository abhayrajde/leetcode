class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        min1 = 100000000000
        for i in range(len(nums)-2):
            low = i+1
            high = len(nums)-1
            while(low<high):
                temp = nums[i]+nums[low]+nums[high]
                if(temp>target):
                    temp1 = temp-target
                    min1 = min(min1,temp1)
                    if(min1 == temp1):
                        mintemp = temp
                    high-=1
                    
                elif(temp<target):
                    temp1 = target-temp
                    min1 = min(min1,temp1)
                    if(min1 == temp1):
                        mintemp = temp
                    low+=1
                    
                else:
                    return(target)
        return(mintemp)
                
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        