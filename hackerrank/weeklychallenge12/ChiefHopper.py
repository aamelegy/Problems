input()
n=[int(x) for x in raw_input().strip().split()]

def isneg(e,n):
    for i in range(len(n)):
        e=2*e-n[i]
    return e/abs(e)

l=0
h=100000
while l<h:
    m=(h+l)/2
    if isneg(m,n)==-1:
        if l==m:
            break
        l=m
    else:
        h=m
print m+1
        
        