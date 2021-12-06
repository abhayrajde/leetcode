class Solution(object):
    def generate(self, numRows):
        list1 = []
        
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                if(j==0 or j == i):
                    temp.append(1)
                else:
                    temp.append(list1[i-1][j-1]+list1[i-1][j])
            list1.append(temp)
        return(list1)
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        