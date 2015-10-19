

class MarbleNecklace():
    def normalize(self, necklace):
        words=[]
        for i in range(len(necklace)):
            words.append(necklace[i::]+necklace[0:i])
            words.append((necklace[i::]+necklace[0:i])[::-1])
        words.sort()
        return words[0]
