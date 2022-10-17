class Solution(object):
    def exist(self, board, word):

        rows = len(board)
        cols = len(board[0])
        
        visited = set()
        
        #r,c is for position in the board matrix and i is for letter position in word
        def backtrack(r,c,i):
            if i == len(word):
                return True
            
            if(r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or board[r][c] != word[i]):
                return False
            
            visited.add((r,c))
            
            #TODO - business logic
            # check left, up, right, down elements i board
            res = (backtrack(r,c-1,i+1) or backtrack(r-1,c,i+1) or backtrack(r,c+1,i+1) or backtrack(r+1,c,i+1))
            
            visited.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack(r,c,0):
                    return True
        return False

        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        