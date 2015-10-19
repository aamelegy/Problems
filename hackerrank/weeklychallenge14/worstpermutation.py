
import sys
n,k=[int(x) for x in raw_input().strip().split()]
num=[int(x) for x in raw_input().strip().split()]

d=dict()
for i in range(len(num)):
    d[num[i]]=i
snum=list(sorted(num))[::-1]
c=0
for i in range(len(num)):
    if k==0:
        print " ".join(map(str,num))
        sys.exit()
    x,y=d[snum[i]],i
    if num[x]!=num[y]:
        num[x],num[y]=num[y],num[x]
        d[num[y]]=y
        d[num[x]]=x
        k-=1
print " ".join(map(str,num))
    
    
        