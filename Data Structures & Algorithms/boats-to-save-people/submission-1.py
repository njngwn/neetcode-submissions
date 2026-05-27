class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left, right = 0, len(people)-1
        num_boat = 0

        people.sort()

        while left < right:
            if people[left] + people[right] > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            
            num_boat += 1
        
        return num_boat+1 if left == right else num_boat