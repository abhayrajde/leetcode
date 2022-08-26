class Solution(object):
    def minSwaps(self, s):
        def countswaps(start):
            countwrong = 0
            
            for c in s:
                if(start != c):
                    countwrong+=1
                if(start == "1"):
                    start = "0"
                else:
                    start = "1"
            return(countwrong//2)
        
        c1 = s.count("1")
        c0 = len(s) - c1
        
        if(abs(c1-c0)>1):
            return -1
        if(c0>c1):
            return countswaps("0")
        if(c0<c1):
            return countswaps("1")
        return(min(countswaps("0"),countswaps("1")))
        """
        :type s: str
        :rtype: int
        """
        