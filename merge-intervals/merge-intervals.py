class Solution(object):
    def merge(self, intervals):
        list1 = []
        intervals = sorted(intervals,key = lambda x:x[0])
        i = 0
        while(i<len(intervals)-1):
            if(intervals[i][1]>=intervals[i+1][0]):
                intervals[i] = [intervals[i][0],max(intervals[i+1][1],intervals[i][1])]
                intervals.remove(intervals[i+1])
                # i+=1
            else:
                i+=1
        return(intervals)
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        