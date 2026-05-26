class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        
        for a, b in zip(word1, word2):
            merged += a + b
        
        remaining = min(len(word1), len(word2))
        merged += word1[remaining:] + word2[remaining:]

        return merged