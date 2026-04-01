class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = len(temperatures)
        result = [0] * days

        for i in range(days):
            for j in range(i, days):
                if temperatures[j] > temperatures[i]:
                    result[i] = j-i
                    break

        return result