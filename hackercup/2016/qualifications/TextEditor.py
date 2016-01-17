
def prefix(w1,w2):
    for i in range(min(len(w1),len(w2))):
        if w1[i] != w2[i]:
            break
    return i

def calc(words):
    sm=words[0]
    for i in range(1,len(words)):
        sm+=len(words[i])-prefix(words[i-1,i])
    return sm

def dfs(start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        print vertex.value
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(vertex.children - visited)
    return visited

class Node():
    def __init__(self,value,children):
        self.value = value
        self.children = children

fout=open("out","w")
fin =open("in")
t=int(fin.readline())
for case in range(1,t+1):
    print "case "+str(case)
    words=[]
    n,k=map(int,fin.readline().strip().split())
    d=dict()
    current=d
    roots=set()
    for i in range(n):
        word=fin.readline().strip()
        words.append(word)
        new=0
        current = roots
        for char in word:
            if char not in [x.value for x in current]:
                node=Node(char,set())
                current.add(node)
            else:
                node=filter(lambda x:x.value == char,current)[0]
            current = node.children
        current.add(Node("-1",set()))
        current = roots
    for node in roots:
        dfs(node)
    print "x"













