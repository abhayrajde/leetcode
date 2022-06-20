class Solution(object):
    def candy(self, ratings):
        lr = [1]*len(ratings)
        rl = [1]*len(ratings)
        # tot = [1]*len(ratings)
        for i in range(1,len(ratings)):
            if(ratings[i]>ratings[i-1]):
                lr[i] = 1 + lr[i-1]
        for i in range(len(ratings)-2,-1,-1):
            if(ratings[i] > ratings[i+1]):
                rl[i] = 1 + rl[i+1]
        tot = 0
        for i in range(len(ratings)):
            tot += max(lr[i],rl[i])
        return(tot)
        
        """
        :type ratings: List[int]
        :rtype: int
        """
        