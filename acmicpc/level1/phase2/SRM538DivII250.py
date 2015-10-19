

class LeftOrRight():
    def maxDistance(self, program):
        l=0 ;r=0 ; mx=0
        for i in program:
            if i=='L':
                l+=1
                r+=1
            elif i=='R':
                r-=1
                l-=1
            elif i=='?':
                l+=1
                r-=1
            mx=max(l,abs(r),mx)
        return mx   