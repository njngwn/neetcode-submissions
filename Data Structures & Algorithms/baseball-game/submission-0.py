class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []

        for oper in operations:
            match oper:
                case '+':
                    records.append(int(records[-1]) + int(records[-2]))
                case 'D':
                    records.append(int(records[-1]) * 2)
                case 'C':
                    records.pop()
                case _:
                    records.append(int(oper))

        return sum(records)