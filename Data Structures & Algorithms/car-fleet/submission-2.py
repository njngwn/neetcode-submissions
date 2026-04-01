class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = [] # stack
        cars = sorted(zip(position, speed), reverse=True)
        print(cars)

        for p, s in cars:
            time = (target - p) / s

            if not fleet or time > fleet[-1]:
                fleet.append(time)

        return len(fleet)