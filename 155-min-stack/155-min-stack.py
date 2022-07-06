class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val):
        self.stack.append(val)
        if(not self.minstack):
            self.minstack.append(val)
        else:
            self.minstack.append(min(val,self.minstack[-1]))
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        self.stack.pop()
        self.minstack.pop()
        """
        :rtype: None
        """
        

    def top(self):
        return(self.stack[-1])
        """
        :rtype: int
        """
        

    def getMin(self):
        return(self.minstack[-1])
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()