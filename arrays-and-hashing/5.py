from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: # type: ignore
        count = defaultdict(int)
        freq = [[] for i in range(0, len(nums) + 1)]   # freq = [[],[],[],...,[]] -> each list is distinct
        res = []

        for n in nums:
            count[n] += 1
        
        for c in count:     # swap keys and values: (num, count) <-> (count, num)
            freq[count[c]].append(c)

        for i in range(len(nums), 0, -1):     # right to left
            for n in freq[i]:       # for each num with freq
                res.append(n)
                k -= 1
                if k == 0:
                    return res
            
        return res