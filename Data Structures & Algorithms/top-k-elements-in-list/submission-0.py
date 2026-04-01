from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = Counter(nums)
        frequency = [[] for _ in range(len(nums)+1)]
        ans = []

        for num, freq in num_counter.items():
            frequency[freq].append(num)
        
        i = len(frequency)-1
        while len(ans) < k:
            ans += frequency[i]
            i -= 1

        return ans