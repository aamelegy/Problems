'''
Created on Sep 8, 2015

@author: sshadmin
'''
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        d=dict()
        for i in range(len(nums)):
            for j in range(nums[i]-t ,nums[i]+t+1):
                if j in d and i-d[j]<=k:
                        return True
            else:
                d[nums[i]]=i
        return False