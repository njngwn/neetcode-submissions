from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        length = 0
        window = Counter()

        for right in range(len(s)):
            # add new element to window
            window[s[right]] += 1

            # move left pointer
            while (right - left + 1) - max(window.values()) > k:
                window[s[left]] -= 1
                left += 1
            
            # update the length
            length = max(length, right - left + 1)

        return length