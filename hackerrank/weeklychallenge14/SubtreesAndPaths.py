
class Node():
    def __init__(self,id):
        self.id=id
        self.val=0
        self.parent=None
        self.neighbors=[]
        self.h=1
n=input()
nd=dict()
for i in range(1,n+1):
    nd[i]=Node(i)
for _ in range(n-1):
    n1,n2=[int(x) for x in raw_input().strip().split()]
    nd[n1].neighbors.append(nd[n2])
    nd[n2].neighbors.append(nd[n1])
s=[nd[1]]
while len(s)>0:
    tn=s.pop()
    for neig in tn.neighbors:
        if not tn.parent or neig.id!=tn.parent.id:
            neig.parent=tn
            neig.h=tn.h+1
            s.append(neig)
    tn.neighbors=[]
q=input()
for _ in range(q):
    line=raw_input().strip().split()
    t,a1,a2=line[0],int(line[1]),int(line[2])
    if t=="add":
        nd[a1].val+=a2
    elif t=="max":
        sm1=0
        node1=nd[a1]
        node2=nd[a2]
        if node1.h>node2.h:
            node1,node2=node2,node1
        diff=node2.h-node1.h
        tmp2=node2
        tmp1=node1
        for _ in range(diff):
            tmp2=tmp2.parent
        maxh=tmp1.h
        while tmp1 != tmp2 and tmp1:
            tmp1=tmp1.parent
            tmp2=tmp2.parent
        maxh=tmp1.h
        
        tmp=node1
        while tmp:
            sm1+=tmp.val
            if sm1<0 and tmp.h>maxh:
                sm1=0
            tmp=tmp.parent
            
        tmp=node2
        sm2=0
        while tmp:
            sm2+=tmp.val
            if sm2<0 and tmp.h>maxh:
                sm2=0
            tmp=tmp.parent
            
        print max(sm1,sm2)    
# for _ in range(q):
#     line=raw_input().strip().split()
#     t,a1,a2=line[0],int(line[1]),int(line[2])
#     if t=="add":
#         nd[a1].val+=a2
#     elif t=="max":
#         sm1=0
#         tmp=nd[a1]
#         while tmp:
#             sm1+=tmp.val
#             tmp=tmp.parent
#             if sm1<0 and tmp:
#                 sm1=0
#         tmp=nd[a2]
#         sm2=0
#         while tmp:
#             sm2+=tmp.val
#             tmp=tmp.parent
#             if sm2<0 and tmp:
#                 sm2=0
#         print max(sm1,sm2)    