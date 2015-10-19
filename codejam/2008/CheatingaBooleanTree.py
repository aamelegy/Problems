
class Node():
    def __init__(self,gate=None,change=None,value=None):
        self.gate=gate
        self.change=change
        self.value=value
def rec(tr,i,v):
    if tr[i].value==v:
        return 0
    elif i >= ((m+1)/2) -1:
        if tr[i].value!=v:
            return 9999999999999
    elif (v==0 and tr[i].gate==1) or (v==1 and tr[i].gate==0):
        return min(rec(tr,i*2+1,v),rec(tr,i*2+2,v))
    elif (v==0 and tr[i].gate==0 and tr[i].change==1) or (v==1 and tr[i].gate==1 and tr[i].change==1):
        return 1+min(rec(tr,i*2+1,v),rec(tr,i*2+2,v))
    elif (v==0 and tr[i].gate==0 and tr[i].change==0) or (v==1 and tr[i].gate==1 and tr[i].change==0):
        return rec(tr,i*2+1,v)+rec(tr,i*2+2,v)
def solve(tr,v,m):
    for i in range(((m-1)/2)-1,-1,-1):
        if (tr[i].gate==1 and (tr[i*2+1].value==1 and tr[i*2+2].value==1)) or (tr[i].gate==0 and (tr[i*2+1].value==1 or tr[i*2+2].value==1)):
            tr[i].value=1
        else:
            tr[i].value=0
    x=rec(tr,0,v)
    if x>9999999999:
        return "IMPOSSIBLE"
    else:
        return x
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    line=fin.readline().strip().split(' ')
    m=int(line[0]) ; v=int(line[1])
    tr=[]
    for i in range((m-1)/2):
        line=fin.readline().strip().split(' ')
        tr.append(Node(int(line[0]),int(line[1])))
    for i in range((m+1)/2):
        line=fin.readline().strip()
        tr.append(Node(value=int(line)))
    fout.write("Case #"+str(case)+": "+str(solve(tr,v,m))+"\n")