class Solution(object):
    def mirrorReflection(self, p, q):
        while p % 2 == 0 and q % 2 == 0:
            p /= 2
            q /= 2
        if q % 2 == 0 and p % 2 != 0:
            return 0
        if q % 2 != 0 and p % 2 == 0:
            return 2
        if q % 2 != 0 and p % 2 != 0:
            return 1
        return -1
        
            
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        