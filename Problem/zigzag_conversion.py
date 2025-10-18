class Solution:
    def convert(self, s: str, numRows: int) -> str:
        def formula(x: int):
            return 2 * x - 2

        def diff(i, j):
            if i > j:
                return j - i
            else:
                return j - i

        if numRows == 1:
            return s

        final_result = []
        formulaY = formula(numRows)

        for i in range(numRows):
            if i >= len(s):
                break

            final_result.append(s[i])

            numA = formulaY - (2 * i)
            numB = diff(numA, formulaY)

            tempIdx = i

            while tempIdx < len(s):
                if numA > 0:
                    tempIdx += numA
                    if tempIdx >= len(s):
                        break
                    else:
                        final_result.append(s[tempIdx])

                if numB > 0:
                    tempIdx += numB
                    if tempIdx >= len(s):
                        break
                    else:
                        final_result.append(s[tempIdx])

        return "".join(final_result)
