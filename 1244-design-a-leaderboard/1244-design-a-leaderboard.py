class Leaderboard(object):

    def __init__(self):
        self.score_board = defaultdict(int)
        

    def addScore(self, playerId, score):
        self.score_board[playerId] = self.score_board.get(playerId,0) + score
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        

    def top(self, K):
        top_scores = sorted(self.score_board.items(), key = lambda x : x[1], reverse = True)
        res = 0
        for i in range(K):
            res += top_scores[i][1]
        return res
        """
        :type K: int
        :rtype: int
        """
        

    def reset(self, playerId):
        del self.score_board[playerId]
        """
        :type playerId: int
        :rtype: None
        """
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)