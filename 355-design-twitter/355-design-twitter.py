class Twitter(object):

    def __init__(self):
        self.count = 0
        self.tweetmap = defaultdict(list) # userId -> list of [count, tweetIds]
        self.followmap = defaultdict(set) # userId -> set of followeeId
        

    def postTweet(self, userId, tweetId):
        self.tweetmap[userId].append([self.count,tweetId])
        self.count-=1
        
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        

    def getNewsFeed(self, userId):
        res = []  # ordered starting from recent
        minheap = []
        
        self.followmap[userId].add(userId)
        for followeeId in self.followmap[userId]:
            if(followeeId in self.tweetmap):
                index = len(self.tweetmap[followeeId])-1
                count, tweetId = self.tweetmap[followeeId][index]
                minheap.append([count, tweetId, followeeId,index-1])
        
        heapq.heapify(minheap)
        while(minheap and len(res)<10):
            count,tweetId,followeeId,index = heapq.heappop(minheap)
            res.append(tweetId)
            if(index>=0):
                count, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minheap,[count, tweetId, followeeId, index-1])
        return(res)
                
        """
        :type userId: int
        :rtype: List[int]
        """
        

    def follow(self, followerId, followeeId):
        self.followmap[followerId].add(followeeId)
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        

    def unfollow(self, followerId, followeeId):
        if(followeeId in self.followmap[followerId]):
            self.followmap[followerId].remove(followeeId)
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)