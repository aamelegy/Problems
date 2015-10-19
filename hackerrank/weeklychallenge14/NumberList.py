
def num_sublists(size):
    return (size*(size+1))/2
t=input()
for _ in range(t):
    n,k=[int(x) for x in raw_input().strip().split()]
    num=[int(x) for x in raw_input().strip().split()]
    cr=0
    sm=0
    for i in range(len(num)):
        if num[i]<=k:
            cr+=1
        else:
            sm+=num_sublists(cr)
            cr=0
    if cr!=0:
        sm+=num_sublists(cr)
    print num_sublists(n)-sm
        
        
    
            
        