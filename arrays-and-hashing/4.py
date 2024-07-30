from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # type: ignore
        strMap = defaultdict(list)

        for s in strs:
            letterCount = [0] * 26
            for c in s:
                letterCount[ord(c) - ord("a")] += 1
            strMap[tuple(letterCount)].append(s)

        return strMap.values()