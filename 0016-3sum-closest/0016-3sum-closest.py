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
        #FOUND THIS SOLUTION IN DISCUSSION, WHICH IS IS KINDOFF EASIER AND MORE APPROACHABLE
        #GETTING THE ABSOLUTE VALUE IN BOTH THE WAY MAKES THIS SOLUTION MORE APPROACHABLE AND EASY
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
            
        return result
        """        
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        