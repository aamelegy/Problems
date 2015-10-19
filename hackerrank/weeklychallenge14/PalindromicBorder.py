

word=raw_input()
pd=dict()
for i in xrange(len(word)):
    s,e=i,i
    while s>=0 and e<len(word) and word[s]==word[e]:
        try:
            pd[word[s:e+1]]+=1
        except:
            pd[word[s:e+1]]=1
        s,e=s-1,e+1
for i in xrange(len(word)-1):
    s,e=i,i+1
    while s>=0 and e<len(word) and word[s]==word[e]:
        try:
            pd[word[s:e+1]]+=1
        except:
            pd[word[s:e+1]]=1
        s,e=s-1,e+1
c=0
for key in pd:
    c+=((pd[key]-1)*(pd[key]))/2
    if c>=1000000007:
        c%=1000000007
print c
        
                
            
            