class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s=s.lower()
        t=t.lower()
        chars = [0]*26
        #Increases by 1
        for c in s:
            idx= ord(c)-ord('a')
            chars[idx]+=1
        for c in t:
            idx= ord(c)-ord('a')
            chars[idx]-=1
        #if both strings are anagram then all 26 must be 0.
        for c in chars:
            if c!=0:
                return False
        return True