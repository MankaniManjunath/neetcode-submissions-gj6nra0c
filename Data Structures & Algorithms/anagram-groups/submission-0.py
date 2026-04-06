class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps ={}
        for s in strs:
            s=s.lower()
            chars = [0]*26
            for c in s:
                idx= ord(c)-ord('a')
                chars[idx]+=1
            key = tuple(chars)
            if key not in maps:
                maps[key]=[]
            maps[key].append(s)
        return list(maps.values())