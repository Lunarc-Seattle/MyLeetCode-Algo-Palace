class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board) # m 是行数
        n = len(board[0])

        def dfs (i, j, k):
            # k 表示：现在正在匹配 word[k]
            # 如果 k 已经等于 word 长度，说明整个单词都匹配完了
            if k == len(word):
                return True
            
            # 越界
            if i<0 or i>= m or j < 0 or j >=n:
                # 因为 Python 下标是从 0 开始的。i = m就已经跑到外面了
                return False
            if board[i][j] != word[k]:
                return False
            
            # 先保存当前字符
            temp = board[i][j]

            # 标记这个格子已经用过
            board[i][j] = "#"
            found = (
                dfs(i+1,j,  k+1) or
                dfs(i,  j+1,k+1) or
                dfs(i-1,j,  k+1) or
                dfs(i,  j-1,k+1) 
            )
            
            # 回溯：恢复现场
            board[i][j] = temp
            return found
        #如果某一次 dfs(...) 返回 True：说明找到了 word 整个函数立刻 return True
        #如果这一次 dfs(...) 返回 False：不进入 if回到 for 循环 继续试下一个格子
        # 如果所有格子都试完了，还是没有 True： 最后 return False
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        
        return False



            
        
