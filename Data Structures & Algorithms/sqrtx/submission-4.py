class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1: return x

        low, high = 1, x // 2
        ans = 1

        while low <= high:
            mid = (low + high) // 2
            res = mid * mid
            # print(f"low: {low}, mid: {mid}, high: {high}, res: {res}")
            if res == x:
                return mid
            elif res < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
