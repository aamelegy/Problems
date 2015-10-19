'''
Created on Sep 19, 2015

@author: sshadmin
'''
#n,k = map(int,raw_input().strip().split())
m=input()
f,s=[],[]
for i in range(m):
    move=input()
    if move < 0 :
        s.append(-move)
    else:
        f.append(move)
if sum(f)>sum(s):
    print "first"
elif sum(s)>sum(f):
    print "second"
else:
    lex=0
    ln = min(len(f),len(s))
    for i in range(ln):
        if f[i]>s[i]:
            lex=True
            break
        elif s[i]>f[i]:
            lex=False
            break
    if lex==0 and len(f)>len(s):
        print "first"
    elif lex==0 and len(s)>len(f):
        print "second"
    elif lex==True:
        print "first"
    elif lex==False:
        print "second"
    elif move >0:
        print "first"
    elif move < 0 :
        print "second"