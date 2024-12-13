class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            ans[key].append(word)
        return list(ans.values())
        
