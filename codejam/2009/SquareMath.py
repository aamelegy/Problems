##not  lexicographically smallest 
from collections import namedtuple
from collections import deque
node=namedtuple("node","value children pos")
state=namedtuple("state","sumn query cop")
d=[(1,0),(-1,0),(0,1),(0,-1)]
def solve(ma,q,v):
    ret=[""]*len(v) 
    vset=set(v)
    c=len(v)
    vi=set()
    while len(q)>0 and c>0:
        node,cstate=q.popleft()
        if node.value!="+" and node.value!="-":
            if cstate.cop=="+":
                n_sum=cstate.sumn+int(node.value)
                query=cstate.query+"+"+node.value
            elif cstate.cop=="-":
                n_sum=cstate.sumn-int(node.value)
                query=cstate.query+"-"+node.value
            else:
                n_sum=int(node.value)
                query=node.value
            n_state=state(n_sum,query,cstate.cop)
            if n_sum in vset:
                ret[v.index(n_sum)]=query
                vset.remove(n_sum)
                c-=1
        else:
            n_state=state(cstate.sumn,cstate.query,node.value)
        for child in node.children:
            if not (child.pos ,n_state.sumn,n_state.cop) in vi:
                q.append((child,n_state))
                vi.add((child.pos ,n_state.sumn,n_state.cop))
    return "\n"+"\n".join(ret)
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    ma=dict() ;q = deque()
    l=fin.readline().strip().split(' ')
    n=int(l[0]);m=int(l[1])
    for i in range(n):
        l=fin.readline().strip()
        for j in range(n):
            ma[(i,j)]=node(l[j],[],(i,j))
            if l[j]!="+" and l[j] !="-":
                q.append((ma[(i,j)],state(0,"",None)))
    for i in range(n):
        for j in range(n):
            p=ma[(i,j)]
            for df in d:
                if df[0]+i<n and df[0]+i>=0 and df[1]+j<n and df[1]+j>=0:
                    c=ma[(df[0]+i,df[1]+j)]
                    p.children.append(c)
    v=[int(x) for x in fin.readline().strip().split(' ')]
    fout.write("Case #"+str(case)+": "+str(solve(ma,q,v))+"\n")