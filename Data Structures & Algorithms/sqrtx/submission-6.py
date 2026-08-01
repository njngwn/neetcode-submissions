class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        ans = 0

        while start <= end:
            n = start + (end - start) // 2
            if x >= n * n:
                start = n+1
                ans = max(ans, n)
            else:
                end = n-1
        return ans