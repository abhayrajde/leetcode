class Solution(object):
    def threeSum(self, nums):   
        # O(N^2) SOLUTION
        nums.sort()
        output_list = []
        for i in range(len(nums)-2):
            if(i == 0 or (nums[i]!=nums[i-1])):
                low = i+1
                high = len(nums)-1
                sum1 = -(nums[i])
                while(low < high):
                    if(nums[low]+nums[high]==sum1):
                        temp = [nums[i],nums[low],nums[high]]
                        output_list.append(temp)
                        while(low<high and (nums[low]==nums[low+1])):
                            low+=1
                        while(low<high and (nums[high-1]==nums[high])):
                            high-=1
                        low+=1
                        high-=1
                    elif(nums[low] + nums[high] < sum1):
                        low+=1
                    else:
                        high-=1
        return(output_list)
                        
        
        
        
        
        
        
        
        
        
        
        
        """
        set1 = set(nums)
        op = []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                temp = [nums[i],nums[j]]
                sum1 = -(nums[i]+nums[j])
                if(sum1 in set1):
                    temp.append(sum1)
                    temp.sort()
                    a,b,c = temp[0],temp[1],temp[2]
                    # if(a!=b and a!=c and b!=c):
                    if(temp not in op and (a!=b and a!=c and b!=c)):
                        op.append(temp)
                        break
        return(op)
        
        """            
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        