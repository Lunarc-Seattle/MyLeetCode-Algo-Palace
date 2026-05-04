class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        def backtrack(start, path, total):
            ## 如果刚好等于 target，说明找到一个组合
            if total == target:
                res.append(path[:])
                #有了 [:]，复制出来的是一个新的 list
                #因为 path 是一个会一直被修改的 list
                return 
            if total> target:
                return

            #start 的作用是：这一层以后，只能选当前数字或者右边的数字，不能回头选左边的数字。
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                #注意：这里还是 i，不是 i + 1
                # 因为同一个数字可以重复使用
                backtrack(i,path, total+candidates[i])

                #你 append 了一个数字去试这条路，试完以后必须 pop 掉，才能回到上一层，换另一条路试。
                path.pop()
                # 这里pop的不是res，是path
        backtrack(0,[],0)
        #注意这里三个参数
        return res

