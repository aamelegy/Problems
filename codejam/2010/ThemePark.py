#small
def cmp_list(a,b):
    for i in range(len(a)):
        if a[i]!=b[i]:
            return False
    return True

def isfound(g,rides):
    for i in range(len(rides)):
        if cmp_list(rides[i],g):
            return i
    return False
            
                    
def solve(r,k,g):
    rides=[]
    rides.append([g,0])
    for ride in range(1,r+1):
        per=0
        n_g=[] ; c=0
        for gr in g:
            c+=1
            if per+gr<=k:
                per+=gr
            else:
                break
        n_g.extend(g[c-1::])
        n_g.extend(g[0:c-1])
        g=n_g
        x=isfound(g,rides)
        if not x==False:
            revenue=rides[len(rides)-1][1]-rides[x-1][1]
            leng=ride-x+1
            left=ride-4+1
            if left >= len:
                revenue=revenue*(left/10)
                still=left%leng
                revenue+=rides[x-1+still][1]-rides[x-1][1]
                revenue+=rides[len(rides)-1][1]
                return revenue
            else:
                still=left%len
                revenue+=rides[x-1+still][1]-rides[x-1][1]
                revenue+=rides[len(rides)-1][1]
                return revenue
        rides.append([g,per+rides[len(rides)-1][1]])
    return rides[len(rides)-1][1]

fin=open('in','r') ; fout=open('out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    line=fin.readline().strip().split(' ')
    r,k=int(line[0]),int(line[1])
    g=[int(x) for x in fin.readline().strip().split(' ')]
    fout.write("Case #"+str(case)+": "+str(solve(r,k,g))+"\n")