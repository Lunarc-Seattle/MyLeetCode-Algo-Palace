class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        # use list rather than []
        i,j =0,0
        # needs 2 0

        while i<len(word1) and j < len(word2): 
        # while needs iterate and " : " 
            result.append(word1[i])
            result.append(word2[j])
            i+=1
            j+=1

        result.append(word1[i:])
        result.append(word2[j:])
        return ''.join(result)
        # toString
