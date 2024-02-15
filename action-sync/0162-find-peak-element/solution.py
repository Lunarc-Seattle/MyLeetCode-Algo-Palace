############################################################
# L0162.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2023
###########################################################
############################################################
# All imports
###########################################################
from typing import List

############################################################
# You cannot change anything in Solution
###########################################################
class Solution:
    def findPeakElement(self, nums: List[int]) -> 'int':
        work = [0]
        ans = [-1]
        show = False
        if (True):
            b = L0162(nums,ans,work,show,"n time constant space")
        if (False):
            b = L0162(nums,ans,work,show,"logn time logn space")
        if (False):
            b = L0162(nums,ans,work,show,"logn time constant space")
        return ans[0]

############################################################
# You cannot change anything in L0162
###########################################################
class L0162:
    def __init__(self,a: List[int],ans: 'list of size 1', work:'list of size 1',show:'bool', alg:'string') -> None:
        self._a = a
        self._ans = ans
        self._work = work
        self._show = show
        self._l = len(a)
        Algorithm(self,alg)

    def __len__(self):
        return self._l;

    def __getitem__(self,i:'int')->'int':
        assert(i >= 0 and i < self._l)
        self._work[0] = self._work[0]+1 
        return self._a[i]

    def set_ans_index(self,i:'int')->'none':
        assert(i >= 0 and i < self._l)
        self._ans[0] = i

    def show(self)->'bool':
        return self._show

class Algorithm:
    def __init__(self,s:'L0162', alg:'string') -> None: 
        self._s = s

        if (alg == "n time constant space"):
            self._n_time_constant_space()
        elif (alg == "logn time logn space"):
            self._logn_time_logn_space()
        elif (alg == "logn time constant space"):
            self._logn_time_constant_space()
        else:
            assert(False)

    def show(self)->'bool':
        return self._s.show()

    ########################################
    # WRITE CODE BELOW
    #########################################

  
    ########################################
    # TIME:O(N)
    # Space:THETA(1)
    #  
    #########################################
    def _n_time_constant_space(self):
        n = len(self._s) 
        for i in range(0, n-1):
            if self._s[i] > self._s[i+1]:
                self._s.set_ans_index(i)
                return;
        self._s.set_ans_index(n-1)
        


    ########################################
    # TIME:O(log n)
    # Space:O(logn )
    #########################################
    def _logn_time_logn_space(self)->'None':
        n = len(self._s)
        
        def binary_search(low, high):
            if low == high:
                self._s.set_ans_index(low)
            elif low < high:
                mid = (low + high) // 2
                if self._s[mid] > self._s[mid + 1]:
                    binary_search(low, mid)
                else:
                    binary_search(mid + 1, high)
        binary_search(0, n-1)
        
        
        
    ########################################
    # TIME:O(log N)
    # Space:THETA(1)
    #########################################
    def _logn_time_constant_space(self)->'None':
        n = len(self._s) 
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if self._s[mid] > self._s[mid + 1]:
                high = mid
            else:
                low = mid + 1
        self._s.set_ans_index(low)

        
