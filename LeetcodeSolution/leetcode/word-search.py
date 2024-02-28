class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # # Count number of letters in board and store it in a dictionary
        # word_length=len(word)
        # boardDic = defaultdict(int)
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         boardDic[board[i][j]] += 1
        # print(boardDic)
        # # Count number of letters in word
        # # Check if board has all the letters in the word and they are atleast same count from word
        # wordDic = Counter(word)
        # for c in wordDic:
        #     if c not in boardDic or boardDic[c] < wordDic[c]:
        #         return False
        # #Traverse through board and if word[0] == board[i][j], call the DFS function
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if board[i][j] == word[0]:
        #             if self.dfs(i, j, 0, board, word):
        #                 return True
        # def dfs(i, j, board, word):
        #     if j-1<0 or i-1<0 or i+1>len(board[0]) or j+1>len(board):
        #         return
        #     if j-1>=0:
        #         dfs(i,j-1,board,word)
        cols,row=len(board[0]),len(board)
        path=set()
        def dfs(r,c,i):
            if i==len(word):
                return True
            if(r<0 or c<0 or r>=row or c>=cols or word[i]!=board[r][c] or (r,c) in path):
                return False
            path.add((r,c))
            res=(dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or 
            dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            path.remove((r,c))
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False



	