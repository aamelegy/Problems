class Pronunciation():
    def canPronounce(self, words):
        vowel={'a','e','i','o','u'}
        for word in words:
            orig=word
            word=word.lower()
            cons_count=0
            vowel_count=0
            last_ch=''
            for ch in word:
                if ch not in vowel:
                    cons_count+=1
                    if cons_count==3:
                        return orig
                else:
                    cons_count=0
                if ch in vowel:
                    vowel_count+=1
                    if vowel_count==2 :
                        if  ch!=last_ch:
                            return orig
                        else:
                            vowel_count=1
                else:
                    vowel_count=0
                last_ch=ch
        return ""