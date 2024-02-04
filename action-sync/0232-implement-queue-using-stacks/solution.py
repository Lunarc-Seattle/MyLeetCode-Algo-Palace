
class ListNode:
    #NOTHING CAN BE CHANGED HERE
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next
         
            
############################################################
#  class  Slist
###########################################################   
class Slist():
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0 
        
    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################
    
    #############################
    #append： add a node at the end of a slist 
    # time: theta(1)
     # space: theta(1)
    #############################
    
    def append(self,x:'int'):
        self._len = self._len + 1
        self._build_a_node(x,True)
    
    
    #############################
    #prepend： add a node at the end of a slist 
    # time: theta(1)
     # space: theta(1)
    #############################
    def prepend(self, x:'int'):
        self._len = self._len + 1
        self._build_a_node(x,False)
        
    
    #############################
    #delete an elemet in a slist 
    # time: o(n)
    # space: theta(1)
    # [currentnode , prevnode]
    #############################
    
    def _unhook(self, nodes:'list of size 2 ' ) -> 'bool':
        if(nodes[0]):
            currentnode =nodes[0]
            previousnode = nodes[1]
            if ((currentnode == self._first ) and (currentnode == self._last) and (previousnode == None)):
                ##list has only one element
                assert(self._first ==self._last)
                self._first = None
                self._last = None
            elif (currentnode == self._first):
                ##first element being removed and list has more than 1 element 
                assert(self._first.next != None)
                self._first = currentnode.next
            elif (currentnode == self._last):
                ##first element being removed and list has more than 1 element 
                assert(self._first)
                previousnode.next = None
                self._last = previousnode
            else:
                ##you are removing middle element
                assert(self._first)
                assert(self._last)
                previousnode.next = currentnode.next
            self._len = self._len -1
            return True
        else:
            return False
        
    
    
    def delete(self, x:'int')->'bool':
        nodes = self._find(x)
        a= self._unhook(nodes)
        return a ;
    
    
    #############################
    #delete first element in slist 
    # time: theta(1)
    # space: theta(1)
    #############################
    
    def delete_front(self)-> 'bool':
        if (self._first):
            nodes = [self._first, None]
            a = self._unhook(nodes)
            return a ;
            #return self.delete(self._first.val)
        else:
            return False
    
    
    #############################
    #get first element in slist 
    # time: theta(1)
    # space: theta(1)
    #############################
    
    def get_front(self)->'T':
        if (self._first):
            return self._first.val
        else:
            return -1

    
    #############################
    #get last element in slist 
    # time: theta(1)
    # space: theta(1)
    #############################
    
    def get_last(self) ->'T':
        if (self._first):
            assert(self._last)
            return self._last.val
        else: 
            return -1
    
    
    #############################
    #delete last element in slist 
    # time: theta(n)
    # space: theta(1)
    #############################
    def delete_last(self)->'bool':
        if(self._first):
            nodes= [self._first,None]
            #list of [currentnode, prevnode]
            while (nodes[0].next):
                nodes[1] = nodes[0]
                nodes[0] = nodes[0].next;
                
            assert(nodes[0])
            assert(nodes[0].next == None)
            if( nodes[1]):
                assert(nodes[1].next == nodes[0])
                
            a = self._unhook(nodes)
            return a;
        else:
            return False
        
        
    #############################
    # is slist empty
    # time: theta(n)
    # space: theta(1)
    #############################
    
    def is_empty(self) ->'bool':
        s=len(self)
        if (s==0):
            return True
        return False
    
    
    #############################
    #number of elements in a list 
    # time: theta(n)
    # space: theta(1)
    #############################
    
    def __len__(self)-> 'int':
        return self._len
    
    
    #############################
    #build a node and add to end/begining
    # time: theta(1)
    # space: theta(1)
    #this problem can happen
    #self._last.next = n
    #atrribute #
    # if append is true
    #if append is flase
    ############################
    
    def _build_a_node (self,i :'int',append:'bool'=True):
        n = ListNode(i)
        if (self._first == None and self._last == None):
            self._first = n 
            self._last = n
        else: 
            if(append):
                self._last.next=n
                self._last=n
            else:
                n.next = self._first
                self._first = n
                
    
    #############################
    #find an element in slist 
    # time: o(n)
    # space: theta(1)
    #############################
    
    def _find (self,x:'int')-> 'list of [currentnode, prevnode]':
        nodes = [self._first ,None]
        while (nodes[0] != None):
            if(nodes[0].val == x):
                return nodes
            nodes[1] = nodes[0]
            nodes[0] =nodes[0].next
        return nodes            
            
  


############################################################
#  class  MyQueue
#232. Implement Queue using Stacks

# https://leetcode.com/problems/implement-queue-using-stacks/
########################################################### 
class MyQueue:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()
        
    def push(self, x:int) -> None:
        self._s.append(x)
        
    def pop(self) -> int:
        x = self._s.get_front()
        self._s.delete_front()
        return x
    
    def peek(self) -> int:
        return (self._s.get_front())
    
    def empty(self) -> bool:
        l= len(self._s)
        if(l == 0):
            return True
        return False
    


