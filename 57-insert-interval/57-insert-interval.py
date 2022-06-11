class Solution(object):
    def insert(self, intervals, newInterval):
        # list1 = []
        # intervals.append(newInterval)
        intervals = sorted(intervals,key = lambda x:x[0])
        if(intervals == []):
            intervals.append(newInterval)
            return(intervals)
            
        for i in range(len(intervals)):
                
            if(intervals[i][0]>=newInterval[0]):
                intervals.insert(i,newInterval)
            
            elif(i == len(intervals)-1):
                intervals.append(newInterval)
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
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        