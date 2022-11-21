class Solution(object):
    def isPossible(self, target):
        # sum = 0
        maxind = 0
        # Step 1: Find the total sum
        totsum = sum(target)
        
        # Step 2: Find the index of maximum value
        maxval = target[0]
        for i in range(len(target)):
            if target[i] > maxval:
                maxind = i
                maxval = target[i]
        
        # Step 3: Find the differnece sum = tot - maxValue
        diff = totsum - maxval
        
        if target[maxind] == 1 or diff == 1: 
            return True
        
        if diff > maxval or diff == 0 or target[maxind]%diff == 0:
            return False
        
        #Step 4: Update maxValue = maxValue - diff
        target[maxind] = maxval % diff
        
        # Step 5: Repeat till all values equal to 1
        return self.isPossible(target)
        
        
        """
        :type target: List[int]
        :rtype: bool
        """
        