class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def rec(r, c, i):
            if i==len(word):
                return True
            if r<0 or r>=m:
                return False
            if c<0 or c>=n:
                return False
            if (r,c) in visited:
                return False
            if board[r][c]!=word[i]:
                return False
            visited.add((r,c))
            res = False
            for dr, dc in directions:
                res = res or rec(r+dr, c+dc, i+1)
            if not res:
                visited.remove((r,c))
            return res

        res = False
        for r in range(m):
            for c in range(n):
                visited = set()
                res = res or rec(r, c, 0)
        return res

                
        
