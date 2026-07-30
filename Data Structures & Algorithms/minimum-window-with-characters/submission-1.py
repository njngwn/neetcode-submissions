from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        required = len(need)
        satisfied = 0
        window = {}
        min_len = float('inf')
        min_range = (0, 0)
        left = 0

        for right, ch in enumerate(s):
            # expand rightward
            window[ch] = window.get(ch, 0) + 1
            if ch in need and window[ch] == need[ch]:
                satisfied += 1
            
            # shrink while satisfied
            while satisfied == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_range = (left, right)
                
                # remove left charactere
                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    satisfied -= 1
                
                left += 1
        
        if min_len == float('inf'):
            return ""
        else:
            l, r = min_range
            return s[l:r+1]