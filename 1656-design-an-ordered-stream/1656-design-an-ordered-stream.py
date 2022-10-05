from collections import defaultdict
class OrderedStream(object):

    def __init__(self, n):
        self.n = n
        self.stream_dict = defaultdict(str)
        self.pointer = 1
        """
        :type n: int
        """
        

    def insert(self, idKey, value):
        res = []
        self.stream_dict[idKey] = value
        if self.pointer == idKey:
            while self.pointer<=self.n and (self.pointer in self.stream_dict):
                res.append(self.stream_dict[self.pointer])
                self.pointer+=1
        return res
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)