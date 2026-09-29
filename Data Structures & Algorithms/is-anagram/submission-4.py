class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        shash, thash = {}, {}

        for n in range(len(s)):
            shash[s[n]] = 1 + shash.get(s[n],0)
            thash[t[n]] = 1 + thash.get(t[n],0)
        for i in shash:
            if shash[i] != thash.get(i, 0):
                return False
        return True        