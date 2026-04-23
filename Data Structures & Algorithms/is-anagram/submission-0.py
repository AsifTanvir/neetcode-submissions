class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wordCountS = {}
        wordCountT = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            wordCountS[s[i]] = 1 + wordCountS.get(s[i], 0)
            wordCountT[t[i]] = 1 + wordCountT.get(t[i], 0)
        
        return wordCountS == wordCountT
            

        