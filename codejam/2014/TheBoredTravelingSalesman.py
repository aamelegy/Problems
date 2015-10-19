
from copy import deepcopy as copy
class Node():
    def __init__(self,value):
        self.value=value
        self.out_children=[]
        self.return_children=[]
class State():
    def __init__(self,nodes,visited_nodes,root,visited_list,ret):
        self.nodes=nodes
        self.visited_nodes=visited_nodes
        self.root=root
        self.visited_list=visited_list
        self.ret=ret
        
def min_nodes(root,nodes,n):
    q=[]
    vi_no=set()
    vi_no.add(nodes[root])
    v_no_li=[nodes[root]]
    q.append(State(nodes,vi_no,root,v_no_li,0))
    while (len(q)>0):
        state_o=q.pop()
        root=state_o.root
        if len(state_o.visited_list)==len(nodes) and state_o.ret==0:
            return state_o.visited_list
        for i in range(len(state_o.nodes[root].out_children)):
            state=copy(state_o)
            child=state.nodes[root].out_children[i]
            child.return_children.append(nodes[root])
            if child.value not in [x.value for x in state.visited_nodes]:
                state.visited_list.append(child)
            state.visited_nodes.add(child)
            state.ret+=1
            state.nodes[root].out_children.remove(child)
            q.append(State(state.nodes,state.visited_nodes,child.value,state.visited_list,state.ret))
        for i in range(len(state_o.nodes[root].return_children)):
            state=copy(state_o)
            child=state.nodes[root].return_children[i]
            child.out_children.append(nodes[root])
            if child.value not in [x.value for x in state.visited_nodes]:
                state.visited_list.append(child)
            state.visited_nodes.add(child)
            state.ret-=1
            state.nodes[root].return_children.remove(child)
            q.append(State(state.nodes,state.visited_nodes,child.value,state.visited_list,state.ret))
        
    
def solve(zip_code,nodes_dict):
    for key in nodes_dict:
        x=min_nodes(key,nodes_dict,len(zip_code))
        if x:
            return ' '.join([str(z.value) for z in x])
        

fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    n,m=[int(x) for x in fin.readline().strip().split(' ')]
    zip_code=dict()
    nodes_dict=dict()
    for i in range(n):
        zip_code[i+1]=fin.readline().strip()
    for i in range(m):
        f,t=[int(x) for x in fin.readline().strip().split(' ')]
        if f not in nodes_dict:
            nodes_dict[f]=Node(f)
        if t not in nodes_dict:
            nodes_dict[t]=Node(t)
        nodes_dict[f].out_children.append(nodes_dict[t])
    fout.write("Case #"+str(case)+": "+str(solve(zip_code,nodes_dict))+"\n")