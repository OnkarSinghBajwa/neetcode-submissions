class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hstr = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))
            hstr[sortedS].append(s)
        return list(hstr.values())





            

        