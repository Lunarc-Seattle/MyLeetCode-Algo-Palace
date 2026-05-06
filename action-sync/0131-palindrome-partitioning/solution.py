class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []
        
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start):
            #如果 start 走到字符串末尾，说明整个 s 都切完了
            if start == len(s):
                res.append(path[:])
                return
            # start == len(s): 一进去就会触发！ base case！
            #错误： if len(path) == len(s):但 path 里面放的是“切出来的片段”，不是字符。
            # 比如：s = "aab"  path = ["aa", "b"]
            # 这时候：len(path) = 2 len(s) = 3
            # 但其实字符串已经切完了 所以 base case 应该看：if start == len(s):
            # 意思是：切割位置已经走到字符串末尾了。

            for e in range(start+1, len(s)+1):
                piece = s[start:e]
            
                if is_palindrome(piece):
                    path.append(piece)

                    backtrack(e)
                    path.pop()
            
        backtrack(0)
        return res


        
