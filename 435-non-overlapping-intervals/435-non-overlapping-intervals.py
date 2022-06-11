class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals = sorted(intervals, key = lambda x:x[0])
        count = 0
        i = 0
        # for i in range(len(intervals)-1):
        while(i<len(intervals)-1):
            if(intervals[i][1]>intervals[i+1][0]):
                if(intervals[i][1]>intervals[i+1][1]):
                    intervals.remove(intervals[i])
                else:
                    intervals.remove(intervals[i+1])
                count+=1
            else:
                i+=1
        return(count)
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        