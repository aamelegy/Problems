#wrong answer
from collections import namedtuple
light=namedtuple('node', 's w t')
edge=namedtuple('edge', 'light ne node1 node2')
def getWeight(edge,d):
    if edge.light.t>d[edge.node1]:
        temp=edge.light.t
        while edge.light.t>d[edge.node1]:
            temp-=edge.light.s+edge.light.w
            if temp<=d[edge.node1]:
                p=temp ; break
    elif edge.light.t<d[edge.node1]:
        temp=edge.light.t
        last=temp
        while edge.light.t<d[edge.node1]:
            temp+=edge.light.s+edge.light.w
            if temp>=d[edge.node1]:
                p=last ; break
            last=temp
    else:
        p=edge.light.t
    if edge.ne=="n" :
        if edge.node2[0]%2==0:
            if d[edge.node1]>=edge.light.s+p:
                t_d=edge.light.s+edge.light.w-(d[edge.node1]-p)+1
            else:
                t_d=1
        else:
            t_d=2
    elif edge.ne=="e":
        if edge.node1[1]%2==0:
            if d[edge.node1]>=edge.light.s+p:
                t_d=1
            else:
                t_d=edge.light.s-(d[edge.node1]-p)+1
        else:
            t_d=2
    return t_d
def solve(vertices,edges,d,m):
    for i in range(1,vertices):
        for edge in edges:
            if d[edge.node1]!="inf":
                t_d=getWeight(edge,d)
                if d[edge.node2]=="inf":
                    d[edge.node2]=d[edge.node1]+t_d
                elif d[edge.node1]+t_d<d[edge.node2]:
                    d[edge.node2]= d[edge.node1]+ t_d
    return d[(0,m*2-1)]
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    d=dict()
    n,m=[int(x) for x in fin.readline().strip().split(' ')]
    map=[[0]*(m*2)]*(n*2)
    edges=[]
    for i in range(0,n*2,2):
        l=[int(x) for x in fin.readline().strip().split(' ')]
        for j in range(0,m*2,2):
            map[i][j]=light(l[0+j/2*3],l[1+j/2*3],l[2+j/2*3])
            map[i+1][j]=light(l[0+j/2*3],l[1+j/2*3],l[2+j/2*3])
            map[i+1][j+1]=light(l[0+j/2*3],l[1+j/2*3],l[2+j/2*3])
            map[i][j+1]=light(l[0+j/2*3],l[1+j/2*3],l[2+j/2*3])
            d[(i,j)]="inf" ;d[(i+1,j)]="inf";d[(i,j+1)]="inf";d[(i+1,j+1)]="inf"
    d[(len(map)-1,0)]=0
    for i in range(n*2):
        for j in range(m*2):
            if i+1<n*2:
                if i%2==0:
                    light1=map[i][j]
                else:
                    light1=map[i+1][j]
                edges.append(edge(light1,"n",(i+1,j),(i,j)))
            if j+1<m*2:
                if j%2==0:
                    light2=map[i][j]
                else:
                    light2=map[i][j+1]
                edges.append(edge(light2,"e",(i,j),(i,j+1)))
    fout.write("Case #"+str(case)+": "+str(solve(n*m*4,edges,d,m))+"\n")