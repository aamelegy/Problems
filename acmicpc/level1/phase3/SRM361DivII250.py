'''
Created on May 30, 2014

@author: sshadmin
'''
class SearchBox():
    def find(self, text, search, wholeWord, start):
        ls=len(search)
        for i in range(start,len(text)-len(search)+1):
            if text[i:i+ls]==search:
                if wholeWord=='N':
                    return i
                else:
                    if i==0 or text[i-1]==' ':
                        if i+ls==len(text) or text[i+ls]==' ':
                            return i
        return -1
            