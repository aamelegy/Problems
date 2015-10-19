from __future__ import division
import math
sign = lambda x: math.copysign(1, x)
class node:
    def __init__(self,v,prob,state):
        self.v=v
        self.prob=prob
        self.state=state
def precalculate(x):
    tri=[]
    tri.append([1])
    last=[ node(1,1/2 ,(1,0)),node(1,1/2 ,(0,1))]
    for i in range (1,x):
        print i
        temp=[]
        for j in range (len(last)+1):
            if j==0:
                temp.append(1)
            elif j== len(last):
                temp.append(1)
            else:
                temp.append(last[j].v+last[j-1].v)
        t_nodes=[]        
        for k in range(len(temp)):
            n=node(temp[k],temp[k]/2**(i+1),(k,len(temp)-k-1))
            t_nodes.append(n)
        last=t_nodes
    return last
                
def solve(n,x,y,tri):
    vl=y+1
    hl=(abs(x/2)+abs(y/2)+1)*sign(x)
    df=(4*abs(hl)-2)*(abs(hl)/2)
    dfl=(4*abs(hl)-3)
    if n>=df:
        return 1.0
    else:
        df=(4*(abs(hl)-1)-2)*((float(abs(hl))-1)/2)
        if n<=df:
            return 0.0
        else:
            dl=n-df
            if x==0:
                return 0.0
            probs=precalculate(int(dl))
            prob=0.0
            for p in probs:
                if p.state[0]<=dfl//2 and p.state[1]<=dfl//2: 
                    if hl>0:
                        if p.state[1]>=vl:
                            prob+=p.prob
                    else:
                        if p.state[0]>=vl:
                            prob+=p.prob
                else:
                    if p.state[0]>dfl//2:
                        l=dfl//2
                        r=p.state[0]-dfl//2+p.state[1]
                    if p.state[1]>dfl//2:
                        l=p.state[0]-dfl//2+p.state[1]
                        r=dfl//2
                    if hl>0:
                        if r>=vl:
                            prob+=p.prob
                    else:
                        if l>=vl:
                            prob+=p.prob
            return prob
            
fin=open('in','r') ; fout=open('out','w')
cases=int(fin.readline().strip())
tri=precalculate(1)
for case in range(1,cases+1):
    line=fin.readline().strip().split(' ')
    n,x,y=int(line[0]),int(line[1]),int(line[2])
    fout.write("Case #"+str(case)+": "+str(solve(n,x,y,tri))+"\n")