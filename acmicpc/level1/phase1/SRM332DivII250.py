import re
class TextStatistics():
    def averageLength(self, text):
        words=re.split("[^a-zA-Z]",text)
        words_len=[len(x) for x in words if x!=""]
        if len(words_len)==0:
            return 0
        average=sum(words_len)/len(words_len)
        return average
