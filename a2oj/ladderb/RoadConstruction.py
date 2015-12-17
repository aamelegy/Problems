__author__ = 'a-ahelme'
n,m=map(int,raw_input().strip().split())

f=set()
for i in range(m):
    n1,n2=map(int,raw_input().strip().split())
    f.add(n1)
    f.add(n2)

for i in range(1,n+1):
    if i not in f:
        print n-1
        for j in range(1,n+1):
            if j!=i:
                print i,j
        break


