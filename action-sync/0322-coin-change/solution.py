############################################################
# L0322.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################

############################################################
# All imports
###########################################################
from typing import List
from time import process_time 


class Solution:
    ## YOU CANNOT CHANGE THIS INTERFACE
    ## LEETCODE INTERFACE
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## YOU CANNOT CHANGE ANYTHING IN THIS PROCEDURE
        work = [0]
        changes = [] #If change cannot be given, you must put -1 in changes[0]
        show = False
        p = L0322(coins,amount,changes,work,show)
        num_change = len(changes)
        if (num_change == 1):
            if (changes[0] == -1):
                num_change = -1
        return num_change

class L0322:
    def __init__(self, coins: List[int], amount:'int', changes:'list of int', work:'List of size 1',show:'boolean'):
        #NOTHING CAN BE CHANGED
        self._d = coins
        self._n = amount
        self._ans = changes
        self._work = work
        self._show = show
        # YOU MUST GENERATE V table and k table
        self._v = [] 
        self._k = []
        # You can have any number of data structures here
        # MUST WRITE TWO ROUTINES
        self._alg()
        self._get_solution() 

    def _increment_work(self):
        self._work[0] = self._work[0] + 1


    ############################################################
    # WRITE CODE BELOW
    ###########################################################

    ############################################################
    # TIME (n * k ) = O(n)
    # SPACE O(n)
    ############################################################
    def _alg(self):
        n = self._n
        coins = self._d

        # Initialize arrays to store minimum number of coins needed
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0

        k = [0] * (n + 1)
        # Iterate through all amounts from 1 to n
        for i in range(1, n + 1):
            min_coin = INF
            for coin in coins:
                self._work[0] += 1
                if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    k[i] = coin  # Update k[i] with the coin denomination that minimizes the number of coins for amount i
                    

        self._v = dp
        self._k = k

        # Generate ans table to trace back the solution
        if self._v[n] != float('inf'):
           
            while n > 0:
                coin = self._k[n]
                self._ans.append(coin)
                n -= coin
        else:
            self._ans.append(-1) 
        
                
                


    ############################################################
    # NOTHING CAN BE CHANGED IN THIS ROUTINE BELOW
    ###########################################################
    def _get_solution(self):
        if (self._show):
            a = []
            for i in range(self._n + 1):
                a.append(i)
            print(a)
            print(self._v)
            print(self._k)
        if (self._n < 1000):
            for i in range(self._n + 1):
                if (self._show):
                    print("minimum change for",i,"cents can be achieved using",self._v[i],"coins.")
                self._get_solution1(i)
        else:
            self._get_solution1(self._n)
            
    ############################################################
    # TIME O(n)
    # SPACE THETA(1)
    # How will you give change for p cents
    # WRITE CODE BELOW
    ############################################################
    def _get_solution1(self,p:'int'):
        
        if self._v[p] != float('inf'):
            amount = p
            given = 0
            i=1
            while amount > 0:
                coin = self._k[amount]
                given += coin
                print(
                    f"{i} : Give coin {coin}. So far you have given= {given}. Remaining to give {amount - coin}")
                amount -= coin
                i += 1

        else:
            print(f"{p} : No optimal solution found")
        
