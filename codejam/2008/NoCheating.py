def FindMaxSum(arr,n):
    incl = arr[0]
    excl = 0
    excl_new=0
    for i in range(1,n):
        excl_new=max(incl,excl)
        incl = excl + arr[i]
        excl = excl_new
    return max(incl,excl)

def solve(n,m,seats):
    col=[0]*m
    for i in range(n):
        for j in range(m):
            if seats[i][j]=='.':
                col[j]+=1
    return FindMaxSum(col,len(col))
                    
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    line=fin.readline().strip().split(' ')
    n=int(line[0]);m=int(line[1])
    seats=[]
    for i in range(n):
        seats.append(fin.readline().strip())
    fout.write("Case #"+str(case)+": "+str(solve(n,m,seats))+"\n")