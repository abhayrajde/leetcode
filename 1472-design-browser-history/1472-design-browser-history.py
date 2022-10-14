class BrowserHistory(object):

    def __init__(self, homepage):
        self.history = []
        self.future = []
        self.history.append(homepage)
        """
        :type homepage: str
        """
        

    def visit(self, url):
        self.history.append(url)
        self.future = []
        """
        :type url: str
        :rtype: None
        """
        

    def back(self, steps):
        while steps > 0 and len(self.history)>1:
            self.future.append(self.history.pop())
            steps-=1
        return self.history[-1]
        """
        :type steps: int
        :rtype: str
        """
        

    def forward(self, steps):
        while steps > 0 and self.future:
            self.history.append(self.future.pop())
            steps-=1
        return self.history[-1]
        """
        :type steps: int
        :rtype: str
        """
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)