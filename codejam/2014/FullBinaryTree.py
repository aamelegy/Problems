'''
Created on May 2, 2014

@author: sshadmin
'''

class Node():
    def __init__(self,value):
        self.children=[]
        self.value=value

def max_nodes(parent,root):
    children=[]
    for child in root.children:
        if child!=parent:
            children.append(child)
    if len(children)==1 or len(children)==0:
        return 0
    elif len(children)>=2:
        temp=[]
        for child in children:
            temp.append(max_nodes(root,child))
        temp.sort()
        temp.reverse()
        return 2+temp[0]+temp[1]
            
def solve(nodes):
    mx=0
    for key in nodes:
        mx=max(mx,max_nodes(None,nodes[key]))
    return len(nodes)-mx-1

fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    n=int(fin.readline().strip())
    nodes_dict=dict()
    for i in range(n-1):
        line=[int(x) for x in fin.readline().strip().split(' ')]
        n1=line[0] ; n2=line[1] 
        if n1 not in nodes_dict:
            nodes_dict[n1]=Node(n1)
        if n2 not in nodes_dict:
            nodes_dict[n2]=Node(n2)
        nodes_dict[n1].children.append(nodes_dict[n2])
        nodes_dict[n2].children.append(nodes_dict[n1])    
    fout.write("Case #"+str(case)+": "+str(solve(nodes_dict))+"\n")