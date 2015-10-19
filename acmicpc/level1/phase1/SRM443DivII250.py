

class SoccerLeagues():
    def points(self, matches):
        res=[]
        for i in range(len(matches)):
            points=0
            for j in range(len(matches)):
                if matches[i][j]=="W":
                    points+=3
                if matches[i][j]=="D":
                    points+=1
                if matches[j][i]=="L":
                    points+=3
                if matches[j][i]=="D":
                    points+=1
            res.append(points)
        return res
                    
                
                
    
