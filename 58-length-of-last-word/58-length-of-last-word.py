class Solution(object):
    def lengthOfLastWord(self, s):
        st=s.strip()
        list1 = list(st.split(" "))
        op = len(list1[-1].strip())
        return(op)
        
        
        
        """
        :type s: str
        :rtype: int
        """
        