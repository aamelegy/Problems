

class InsideOut():
    def unscramble(self, line):
        return line[0:len(line)/2][::-1]+line[len(line)/2::][::-1]
