class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix[0])
        row=0
        for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][m-1]:
                row=i
                break
        l=0
        r=m-1
        while l <= r:
            mid = (l+r)//2

            if matrix[row][mid] == target :
                return True
            elif matrix[row][mid] > target :
                r = mid-1
            else :
                l = mid + 1
        return False