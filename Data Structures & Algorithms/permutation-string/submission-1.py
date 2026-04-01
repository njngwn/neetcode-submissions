from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)
        if s1_len > s2_len: return False

        s1_counter = Counter(s1)
        window_counter = Counter(s2[:s1_len])

        if s1_counter == window_counter: return True

        for right in range(s1_len, s2_len):
            # update window
            char_in = s2[right]
            window_counter[char_in] += 1

            char_out = s2[right - s1_len]
            window_counter[char_out] -= 1

            if window_counter[char_out] == 0:
                del window_counter[char_out]

            if s1_counter == window_counter: 
                return True

        return False