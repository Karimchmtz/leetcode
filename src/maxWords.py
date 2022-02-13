class Solution(object):
    def mostWordsFound(self, sentences):
        max = 0
        count = 0
        i = 0
        for sentence in sentences:
            i = 0
            count = 0
            lastChar = None
            while (i < len(sentence)):
                if (sentence[i] == ' '):
                    lastChar = sentence[i]
                    i += 1
                    continue
                
                if (sentence[i] != ' ' and lastChar == None):
                    lastChar = sentence[i]
                    count += 1
                    i += 1
                    continue
                
                if (sentence[i] != ' ' and lastChar == ' '):
                    lastChar = sentence[i]
                    count += 1
                    i += 1
                    continue
                
                else:
                    lastChar = sentence[i]
                    i += 1
            
            if (count > max):
                max = count

        return max