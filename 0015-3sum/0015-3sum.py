class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        
        for i in range(len(nums)-2):
            if(i == 0 or nums[i] !=nums[i-1]):
                low = i+1
                high = len(nums)-1
                tot_sum = -nums[i]
                while(low<high):
                    if(nums[low] + nums[high] == tot_sum):
                        result.append([nums[i],nums[low],nums[high]])
                    
                        while(low<high and (nums[low] == nums[low+1])):
                            low+=1

                        while(low<high and (nums[high] == nums[high-1])):
                            high-=1
                        low+=1
                        high-=1
                    elif(nums[low]+nums[high]<tot_sum):
                        low+=1
                    else:
                        high-=1
        return result
                    
                
            
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        