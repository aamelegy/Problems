import sys
def read_integers():
    return [int(x) for x in raw_input().strip().split(' ')]
def read_binary():
    return [int(x) for x in raw_input().strip()]
n,k=read_integers()
s=read_binary()
if k==1:
    print ''.join(map(str,s))
    sys.exit()
r=[s[0]]
lastk=s[0]
for i in range(1,n):
    nr=s[i]^lastk
    r.append(nr)
    lastk^=nr
    if i-k+1>=0:
        lastk^=r[i-k+1]
print ''.join(map(str,r))