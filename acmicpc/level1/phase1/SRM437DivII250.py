

class TheBeauty():
    def find(self, n):
        distinct=set()
        word=str(n)
        for ch in word:
            distinct.add(ch)
        return len(distinct)
