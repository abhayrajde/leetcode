# take start and end  time in different list array
# Sort both(start,end) list
# If start time for a pointer is less than end time for the pointer in end list
    # increment the room needed count,
    # increment the start pointer
    # store the res as max of count
# Else -- the end pointer time is > start pointer time
    # decrement the room needed count
    # increment thr end time pointer
# Return res
class Solution(object):
    def minMeetingRooms(self, intervals):
        start = []
        end = []
        
        for s,e in intervals:
            start.append(s)
            end.append(e)
        
        start = sorted(start)
        end = sorted(end)
        
        res, count = 0, 0
        s, e = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                count += 1
                res = max(res, count)
            else:
                e += 1
                count -= 1
        return res
                
            
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        