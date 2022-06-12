class Solution(object):
    def exist(self, board, word):
        i,j = len(board),len(board[0])
        visited = set()
        # count = 0
        def dfs(i,j,count):
            
            if(count == len(word)):
                return(True)
            
            if((i>=len(board)) or (j>= len(board[0])) or (i < 0) or (j<0) or ((i,j) in visited) 
               or (word[count] != board[i][j])):
                return(False)
            
            # count+=1
            visited.add((i,j))
            res = (dfs(i+1,j,count+1) or dfs(i-1,j,count+1) or dfs(i,j+1,count+1) or dfs(i,j-1,count+1))
            visited.remove((i,j))
            return(res)
        
        for k in range(len(board)):
            for l in range(len(board[0])):
                if(dfs(k,l,0)):
                    return(True)
        return(False)
            
        """
        i,j = len(board),len(board[0])
        res = False
        visited = set()
        count = 0
        def dfs(i,j,str):
            
            if(str == word):
                res = True
                return
            
            if(i >= len(board) or j >= len(board[0])): 
                return
            
            visited.append([i,j])
            if(board[i][j] == word[count]):
                str+=board[i][j]
                if(board[i+1][j] == word[count+1] and i+1<=len(board)-1 and ([i+1,j] not in visited)):
                    count+=1
                    dfs(i+1,j,str)
                elif(board[i-1][j] == word[count+1] and i-1>=0 and ([i-1,j] not in visited)):
                    count+=1
                    dfs(i-1,j,str)
                elif(board[i][j+1] == word[count+1] and j+1<=len(board[0]) and ([i,j+1] not in visited)):
                    count+=1
                    dfs(i,j+1,str)
                elif(board[i][j-1] == word[count+1] and j-1>=0 and ([i,j-1] not in visited)):
                    count+=1
                    dfs(i,j-1,str)
                count-=1
        """
                
            
            
            
                
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        