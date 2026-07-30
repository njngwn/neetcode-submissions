from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = [] # store index

        for i, num in enumerate(nums):
            # remove index which is out of window range
            if dq and dq[0] <= i - k:
                dq.popleft()
            
            # remove the element which is smaller than new element
            while dq and nums[dq[-1]] < num:
                dq.pop()
            
            dq.append(i)

            # add max value
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result


