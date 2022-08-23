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
        '''
        boxTypes.sort(key=lambda x: -x[1])
        boxes = 0
        for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box
                boxes += box * units
            else:
                boxes += truckSize * units
                return boxes
        return boxes
        '''
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        