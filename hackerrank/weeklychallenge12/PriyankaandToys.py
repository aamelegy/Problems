
input()
toys=[int(x) for x in raw_input().strip().split()]
toys.sort()
last,cost=toys[0],1
for i in range(1,len(toys)):
    if toys[i]>last+4:
        cost+=1
        last=toys[i]
print cost
        
    