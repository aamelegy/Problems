'''
Created on Jun 6, 2014

@author: sshadmin
'''
class TomekPhone():
    def minKeystrokes(self, frequencies, keySizes):
        frequencies,keySizes=sorted(list(frequencies),reverse=True),sorted(list(keySizes),reverse=True)
        i,j,sm,keys=0,0,0,len(keySizes)
        if sum(keySizes)<len(frequencies):
            return -1
        while j<len(frequencies):
            x=i%keys
            if keySizes[x]>0:
                keySizes[x]-=1
                sm+=frequencies[j]* ((i/keys)+1)
                j+=1
            i+=1
        return sm
            