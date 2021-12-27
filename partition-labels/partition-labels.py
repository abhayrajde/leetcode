class Solution(object):
    def partitionLabels(self, s):
        # s = "ababcbacadefegdehijhklij"
        dic1 = {}
        for i in range(len(s)):
            dic1[s[i]] = i+1 
        # print(dic1)
        # max1 = dic1[s[0]]
        i = 0 
        op = []
        while(i < len(s)):
            max1 = dic1[s[i]]
            count = 0
            while(i < max1):
                if(max1 < dic1[s[i]]):
                    max1 = dic1[s[i]]
                count += 1
                # print(count)
                i += 1
            op.append(count)
        # print(op)
        return(op)
        """
        :type s: str
        :rtype: List[int]
        """
        