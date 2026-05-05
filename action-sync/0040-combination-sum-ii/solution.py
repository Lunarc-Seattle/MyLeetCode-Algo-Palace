class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #关于本题不可以重复：
        #res 里的list 内部，可以有重复数字，因为它们来自 candidates 里不同的位置。
        #比如可以有：[1, 1, 6]
        #但是 res 里不能有两个一模一样的 list。
        # 比如不可以这样：[[1, 7],[1, 7]]
        #哪怕第一个 [1,7] 用的是 index 0 的 1，第二个 [1,7] 用的是 index 1 的 1。
        #因为答案只看“数值组合”，不看 index 来源

        candidates.sort()
        res = []
        def backtrack(start,path,total):
            if total == target:
                res.append(path[:])
                return
                #这里的 [:] 就是为了 复制一份当时的 path，把“那一刻的答案快照”放进 res.因为 path 后面会一直被改：
            if total> target:
                return

            for i in range(start, len(candidates)):
                #最重要的一句：去重
                if i>start and candidates[i] == candidates[i-1]:
                    continue
                    # i>start 这里直接保护的是 i == start 的情况
                #在下一层的数字重复是可以的
                #比如：candidates = [1, 1, 6] 第一层选了第一个 1 后，进入下一层： path = [1] start = 1
                path.append(candidates[i])
                backtrack(i+1, path, total+candidates[i])
                path.pop()
        backtrack(0,[],0)
        return res


        
