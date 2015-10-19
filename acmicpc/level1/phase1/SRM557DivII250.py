

class GreatFairyWar():
    def minHP(self, dps, hp):
        damage=0
        total=sum(dps)
        for i in range(len(dps)):
            damage+=total*hp[i]
            total-=dps[i]
        return damage