class Solution:
    def generate(self, numRows: int) -> List[List[int]]: # type: ignore
        triangle = [[1]]
        prevRow = [1]

        for r in range(1, numRows):
            row = [1]
            count = r

            while count > 1:
                sumAbove = prevRow[r - count] + prevRow[r - count + 1]
                row.append(sumAbove)
                count -= 1

            row.append(1)
            triangle.append(row)
            prevRow = row

        return triangle