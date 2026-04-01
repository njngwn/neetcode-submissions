class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # alphabets - string in strs
        
        for s in strs:
            alphabets = [0] * 26 # a-z
            for ch in s:
                alphabets[ord(ch)-ord('a')] += 1
            key = tuple(alphabets) # convert list to tuple for immutablity
            anagrams[key].append(s)

        return list(anagrams.values())