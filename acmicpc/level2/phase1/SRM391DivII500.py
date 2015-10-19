class IsomorphicWords():
    def iso(self,w1):
        mp=dict()
        w=''
        for i in range (len(w1)):
            if w1[i] not in mp:
                mp[w1[i]]=i
            w+=str(mp[w1[i]])
        return w
    def countPairs(self, words):
        c=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if self.iso(words[i])==self.iso(words[j]):
                    c+=1
        return c