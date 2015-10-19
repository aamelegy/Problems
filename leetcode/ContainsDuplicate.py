'''
Created on Sep 8, 2015

@author: sshadmin
'''
class Solution(object):
    def containsDuplicate(self, nums):
        s=set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False