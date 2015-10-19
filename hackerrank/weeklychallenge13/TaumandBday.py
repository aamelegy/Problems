t=input()
for _ in range(t):
    b,w=[int(x) for x in raw_input().strip().split()]
    x,y,z=[int(x) for x in raw_input().strip().split()]
    print b*min(x,y+z)+w*min(y,x+z)