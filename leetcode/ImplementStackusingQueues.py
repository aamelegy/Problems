from collections import deque
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.d1=deque()
        self.d2=deque()
        self.size=0
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.d1.append(x)
        self.size+=1
        

    def pop(self):
        """
        :rtype: nothing
        """
        for i in range(self.size-1):
            self.d2.append(self.d1.popleft())
        self.d1.popleft()
        self.d1,self.d2=self.d2,self.d1
        self.size-=1

    def top(self):
        """
        :rtype: int
        """
        for i in range(self.size-1):
            self.d2.append(self.d1.popleft())
        tmp=self.d1.popleft()
        self.d2.append(tmp)
        self.d1,self.d2=self.d2,self.d1
        return tmp
        
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.size==0:
            return True
        return False
s=Stack()
s.push(1)
s.top()
        