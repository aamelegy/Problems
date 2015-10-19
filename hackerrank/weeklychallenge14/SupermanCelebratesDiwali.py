
n,h,i=[int(x) for x in raw_input().strip().split()]
b=[]
d=[]
mxf=[0]*(h+1)
for _ in range(n):
    f=[int(x) for x in raw_input().strip().split()][1::]
    cb=[0]*(h+1)
    for floor in f:
        cb[floor]+=1
    b.append(cb)
    d.append([0]*(h+1))
    
for fl in range(1,h+1):
    mx=0
    for bi in range(n):
        d[bi][fl]+=b[bi][fl]
        if fl-i>0:
            d[bi][fl]+=max(mxf[fl-i],d[bi][fl-1])
        elif fl-1>0:
            d[bi][fl]+=d[bi][fl-1]
        mx=max(d[bi][fl],mx)
    mxf[fl]=mx
print max([d[x][h] for x in range(n)])
            
        
