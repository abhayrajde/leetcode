class Solution(object):
    def sumSubarrayMins(self, arr):
        left = [0]*(len(arr))
        right = [0]*(len(arr))
        stack = []
        # storing left reach
        for i in range(len(arr)):
            curr_ele = arr[i]
            curr_count = 1
            while stack and stack[-1][0]>arr[i]:
                temp = stack.pop()
                curr_count+= temp[1]
            stack.append((curr_ele,curr_count))
            left[i] = curr_count

        stack = []
        for i in range(len(arr)-1,-1,-1):
            curr_ele = arr[i]
            curr_count = 1
            while stack and stack[-1][0]>=arr[i]:
                temp = stack.pop()
                curr_count+= temp[1]
            stack.append((curr_ele,curr_count))
            right[i] = curr_count
        result = []                
        for i in range(len(arr)):
            result.append(arr[i]*left[i]*right[i])
        print left
        
        print right
        print result
        return sum(result) % (10**9 + 7)
        '''
        #Brute Force TC- N^2
        res = 0
        for i in range(len(arr)-1):
            temp = [arr[i]]
            res+=temp[0]
            for j in range(i+1,len(arr)):
                temp.append(arr[j])
                res+=min(temp)
        res+=arr[-1]
        return res
        '''    
        """
        :type arr: List[int]
        :rtype: int
        """
        