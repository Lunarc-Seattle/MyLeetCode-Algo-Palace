class Solution:
    def countPrimes(self, n: int) -> int:
        list = []
        work = [0]
        if False:
            L0204(n, list, work, "up_to_prime")
        if True:
            L0204(n, list, work, "sieve_of_eratosthenes")
        return len(list)


############################################################
#  L0204 class
############################################################
class L0204:
    def __init__(
        self, n: "int", prime_number_list: "list", work: "list of size 1", alg: "string"
    ):
        self._n = n
        self._prime_number_list = (
            prime_number_list  # You need to append this using _append_prime_number
        )
        self._work = work  # You need to increment using _increment_work_done()
        if alg == "up_to_prime":
            self.up_to_primes()
        elif alg == "sieve_of_eratosthenes":
            self.sieve_of_eratosthenes()
        else:
            assert False

    ############################################################
    # All work done goes through this routine.
    # Nothing can be changed
    ###########################################################
    def _increment_work_done(self):
        self._work[0] = self._work[0] + 1

    ############################################################
    # All prime numbers are appended to the list.
    # Nothing can be changed
    ###########################################################
    def _append_prime_number(self, p):
        self._prime_number_list.append(p)

    ##Required function to implement
    def up_to_primes(self) -> "None":
        ## NOTHING CAN BE CHANGED HERE
        ## you cannot call log from Python library
        self._up_to_primes()

    ##Required function to implement
    def sieve_of_eratosthenes(self) -> "None":
        ## NOTHING CAN BE CHANGED HERE
        ## YOU CANNOT CALL math.log from Python library
        self._sieve_of_eratosthenes()

    ############################################################
    # Implement your code BELOW
    # You can have any number of private variables and functions
    # YOU CANNOT CALL math.log from Python library
    ###########################################################
    
    ############################################################
    # up to prime method 
    # give an ineter n, return thr number of prime numbers that are strickly less than n
    ###########################################################
    def _is_visible_by_prime(self, n:"int", p:"list") -> "bool":
        i=0
        while (p[i]*p[i])<=n:
            self._increment_work_done()
            if n%p[i] ==0:
                return False
            i=i+1
        return True
    
    def _up_to_primes(self):
        if(self._n <3):
            return
        self._append_prime_number(2)
        k=self._n
        for i in range(3, k, 2):
            p=self._is_visible_by_prime(i , self._prime_number_list)
            if p ==True:
                self._append_prime_number(i)
                
    
    ############################################################
    # sieve of eratosthenes method
    # give a ineter n, return thr number of prime numbers that are strickly less than n
    ###########################################################
    def _sieve_of_eratosthenes(self):
        if(self._n<2):
            return
        l=[True]*self._n
        l[0]=False
        l[1]=False
        i=2
        while(i*i)<= self._n:
            if l[i]==True:
                j=i
                while(i*j)<(self._n):
                    self._increment_work_done()
                    l[i*j]=False
                    j=j+1
            i=i+1
        
        for i in range(self._n):
            self._increment_work_done()
            if l[i] ==True:
                self._append_prime_number(i)
                
                
