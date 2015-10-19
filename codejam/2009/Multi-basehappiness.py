happy=set()
def isHappy(n,base):
    if (n,base) in happy:
        return True
    states=set()
    str_n=str(dic[n][base])
    solved=False
    while not solved:
        sum=0
        solved=False
        for ch in str_n:
            sum+=int(ch)**2
        if sum==1:
            solved=True
        str_n=str(dic[sum][base])
        if str_n in states:
            return False
        else:
            states.add(str_n)
    happy.add((n,base))
    return True

def solve(b):
    for i in range(2,150000):
        solved=True
        for ba in b:
            if not isHappy(i,ba):
                solved=False
                break
        if solved:
            return i
def pre():
    for i in range(1,150001):
        print i
        dic[i]=[0]*11
        for j in range(2,len(dic[i])):
            ba=str(dic[i-1][j])
            c=0
            for k in range(len(ba)-1,-1,-1):
                if ba[k]==str(bases[j]-1):
                    c+=1
                else:
                    break
            if c>0:
                st=str(dic[i-1][j]) ;le=len(st)
                l=c ; t=10**l-int(st[le-c:le])
                dic[i][j]=dic[i-1][j]+t
            else:
                dic[i][j]=dic[i-1][j]+1
            
bases=[0,1,2,3,4,5,6,7,8,9,10]
dic=[[0,0,0,0,0,0,0,0,0,0,0]]*15000002 
pre()    
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    bases=[int(x) for x in fin.readline().strip().split(' ')]
    fout.write("Case #"+str(case)+": "+str(solve(bases))+"\n")