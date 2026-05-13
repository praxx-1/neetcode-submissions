class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        m = len(matrix[0])

        row = -1

        t = 0
        b = n - 1

        # Find correct row
        while t <= b:

            mid = (t + b) // 2

            if matrix[mid][0] <= target <= matrix[mid][m - 1]:
                row = mid
                break

            elif target < matrix[mid][0]:
                b = mid - 1

            else:
                t = mid + 1

        if row == -1:
            return False

        # Binary search inside row
        l = 0
        r = m - 1

        while l <= r:

            mid = (l + r) // 2

            if matrix[row][mid] == target:
                return True

            elif matrix[row][mid] > target:
                r = mid - 1

            else:
                l = mid + 1

        return False