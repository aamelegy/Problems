


class RunLengthEncoding():
    def decode(self, text):
        total=0 ; p=0;word=''
        while(p<len(text)):
            current=''
            while(text[p].isdigit()):
                current+=text[p]
                p+=1
            if current=='':
                current='1'
            num=int(current)
            ch=text[p]
            total+=num
            if total>50:
                return "TOO LONG"
            word+=ch*num
            p+=1
        return word