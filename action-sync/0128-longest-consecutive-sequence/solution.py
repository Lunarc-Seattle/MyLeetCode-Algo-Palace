class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num-1 not in num_set:
                cur_num = num
                cur_length = 1
            
                while cur_num+1 in num_set:
                    cur_num += 1
                    cur_length +=1

                longest = max(cur_length, longest)
            
        return longest        
