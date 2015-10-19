'''
Created on Sep 14, 2015

@author: sshadmin
'''
from collections import Counter
s=raw_input().strip()
sc=Counter(list(s))
oddc=0
for key in sc:
    if sc[key] % 2 !=0:
        oddc+=1
if oddc<2:
    print "First"
else:
    if oddc %2 ==0:
        print "Second"
    else:
        print "First"
    