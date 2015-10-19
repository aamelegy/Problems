class Solution(object):
    def isPowerOfTwo(self, n):
        if n<0:
            return False
        c=0
        for _ in range(32):
            if n & 1 ==1:
                c+=1
            n>>=1
        if c==1:
            return True
        else:
            return False
print Solution().isPowerOfTwo(7)
            
        