class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_to_t = dict()
        mapping_to_s = dict()

        for i, j in zip(s, t):
            if (i in mapping_to_t and j != mapping_to_t.get(i)) or (j in mapping_to_s and i != mapping_to_s.get(j)):
                return False
            elif i not in mapping_to_t and j not in mapping_to_s:
                mapping_to_t[i] = j
                mapping_to_s[j] = i


        return True