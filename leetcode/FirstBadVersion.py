# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(version):
    if version >0:
        return True
    else:
        return False
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s,e=1,n
        while s<=e:
            m=(s+e)/2
            if isBadVersion(m) and (m==1 or not isBadVersion(m-1)):
                return m
            elif not isBadVersion(m):
                s=m+1
            else:
                e=m-1
print Solution().firstBadVersion(range(2))
                
        