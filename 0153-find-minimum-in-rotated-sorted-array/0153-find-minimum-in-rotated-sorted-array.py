class Solution(object):
    def findMin(self, nums):
        # 
#         start = 0
#         end = len(nums)-1
#         # mid = (start + end)//2
#         res = nums[0]
#         while end > start:
#             if nums[start] < nums[end]:
#                 res = min(res,nums[start])
#                 break
            
#             mid = (start + end)//2
#             res = min(res,nums[mid])
            
#             if nums[mid] >= nums[start]:
#                 start = mid + 1
            
#             else:
#                 end = mid - 1
#         return res
        l = 0
        r = len(nums)-1
        res = nums[0]
        while(l<=r):
            if(nums[l] < nums[r]):
                res = min(res,nums[l])
                break
            
            m = (l+r)//2
            res = min(res,nums[m])
            if(nums[m]>=nums[l]):
                l = m + 1
            else:
                r = m - 1
        return(res)
            
            
            
                
        """
        :type nums: List[int]
        :rtype: int
        """
        