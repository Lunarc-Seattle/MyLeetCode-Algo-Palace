class Solution:
    #YOU CANNOT CHANGE THIS INTERFACE
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        work = [0]
        # p = L0977("NSquareTime_1_Space",nums,ans,work,False)
        # p = L0977("NlognTime_N_Space",nums,ans,work,False)
        p = L0977("NTime_1_Space",nums,ans,work,False)
        return ans

########################################
#Nothing can be changed in class L0977
########################################
class L0977:
    def __init__(self,alg:'string',a:List[int], ans:List[int], work:'List of size 1', show:'bool'):
        self._a = a ;
        self._ans = ans ;
        self._work = work ;
        self._show = show ;
        algb = AlgL0977(self,alg,ans,show)

    def size(self)->'int':
        return len(self._a)

    def get(self,i:'int'):
        self._work[0] = self._work[0] + 1
        return self._a[i]

    def increment_work(self,i:'int'):
        self._work[0] = self._work[0] + i

########################################
# WRITE CLASS AlgL0977
#YOU CAN HAVE ANY NUMBER OF PRIVATE VARIABLES and FUNCTIONS
########################################
class AlgL0977():
    def __init__(self,h:'L0977',alg:'string', ans:List[int],show:'bool'):
        self._h = h 
        self._ans = ans 
        self._show = show 
        if (alg == "NSquareTime_1_Space"):
            self._alg_NSquareTime_1_Space()
        elif (alg == "NlognTime_N_Space"):
            self._alg_NlognTime_N_Space()
        elif (alg == "NTime_1_Space"):
            self._alg_NTime_1_Space()
        else:
            assert(False)

    ########################################
    #   WRITE YOUR CODE BELOW
    #######################################

    ########################################
    # TIME:O(N^2)
    # Space:O(1)
    #########################################
    def get_smallest (self, p: 'start',n: 'end')->'int':
        small_pos=p
        small_val=self._ans[small_pos]
        for i in range(p,n):
            self._h.increment_work(1)
            if (self._ans[i]<small_val):
                small_pos=i
                small_val=self._ans[i]
        return small_pos
    
    def _alg_NSquareTime_1_Space(self) :
        n = self._h.size()
        if n > 0:
            for i in range(0, n):
                x=self._h.get(i)
                self._ans.append(x*x)
            for i in range(n):
                j=self.get_smallest(i,n)
                if(j!=i):
                    t=self._ans[j]
                    self._ans[j]=self._ans[i]
                    self._ans[i]=t

    ########################################
    # TIME:O(Nlogn)
    # Space:O(N)
    #########################################
    def _alg_NlognTime_N_Space (self) :
        n = self._h.size();
        if (n > 0):
            for i in range(0,n):
                x=self._h.get(i) 
                self._ans.append (x*x)
            self._ans.sort( )
            w = n * math.log(n, 2)
            self._h.increment_work(int (w) )


    ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    #########################################
    def _alg_NTime_1_Space (self):
        n = self._h.size()
        if(n>0):
            for i in range(0,n):
                self._ans.append(i)
            i=0;
            j=n-1;
            k=n-1 ;
            while(i<=j):
                x=self._h.get(i)
                i2=x*x
                y=self._h.get(j)
                #j2=(self._h.get(j))**2
                j2=y*y
                if(j2>i2):
                    self._ans[k]=j2
                    j=j-1
                else:
                    self._ans[k]=i2
                    i=i+1
                k=k-1
            assert (k== -1)


