import sys
t=input()
for _ in range(t):
    n,k=[int(x) for x in raw_input().strip().split()]
    c=[int(x) for x in raw_input().strip().split()]
    dp=[False]*2000
    dp[0]=True
    for i in range(1,k+1):
        for j in range(n):
            if i>=c[j]:
                if dp[i-c[j]]:
                    dp[i]=True
    for i in range(k,-1,-1):
        if dp[i]:
            print i
            break
        
        
    
             
    
    
