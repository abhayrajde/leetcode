class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key = lambda x:x[1], reverse = True)
        # print(boxTypes)
        res = 0
        for boxes, units in boxTypes:
            if(truckSize > boxes):
                res += (boxes*units)
                truckSize -= boxes
            else:
                res += (truckSize*units)
                return res
        return res
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        