class FreqStack(object):

    def __init__(self):
        self.count = {}
        self.maxcount = 0
        self.stacks = {}

    def push(self, val):
        valcount = 1 + self.count.get(val,0)
        self.count[val] = valcount
        if(valcount > self.maxcount):
            self.maxcount = valcount
            self.stacks[valcount] = []
        self.stacks[valcount].append(val)
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        res = self.stacks[self.maxcount].pop()
        self.count[res]-=1
        if(not self.stacks[self.maxcount]):
            self.maxcount-=1
        return(res)
        """
        :rtype: int
        """
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()