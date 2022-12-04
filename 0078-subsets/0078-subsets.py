class Solution(object):
    def subsets(self, nums):
        if not nums:
            return []
        res = []
        curr = []
        def dfs(i,curr):
            if i >= len(nums):
                res.append(curr[:])
                return
            # res.append(curr[:])
            # print(curr + [nums[i]])
            pick = dfs(i+1,curr + [nums[i]])
            not_pick = dfs(i+1,curr)
        dfs(0,[])
        return res
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        