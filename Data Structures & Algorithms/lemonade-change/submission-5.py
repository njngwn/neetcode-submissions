class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_5, bill_10, bill_20 = 0, 0, 0

        for bill in bills:
            # cannot provide the correct change
            if bill == 5:
                bill_5 += 1
            elif bill == 10:
                if bill_5 > 0:
                    bill_5 -= 1
                    bill_10 += 1
                else:
                    return False
            else:
                if bill_5 > 0 and bill_10 > 0:
                    bill_5 -= 1
                    bill_10 -= 1
                    bill_20 += 1
                elif bill_5 >= 3:
                    bill_5 -= 3
                    bill_20 += 1
                else:
                    return False


        return True