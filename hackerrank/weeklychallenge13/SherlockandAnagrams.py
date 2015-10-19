t=input()
for _ in range(t):
    d=dict()
    s=raw_input().strip()
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            sor="".join(sorted(s[i:j]))
            if sor not in d:
                d[sor]=0
            d[sor]+=1
    sm=0
    for key in d:
        n=(d[key]-1)
        sm+=(n*(n+1))/2
    print sm
    
            