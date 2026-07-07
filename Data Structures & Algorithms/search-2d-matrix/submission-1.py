class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        for row in range(n):
            low, high = 0, m - 1

            if target >= matrix[row][low] and target <= matrix[row][high]:
                return self.helper(matrix[row], target)

        return False

    def helper(self, nums: List, target: int) -> bool:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return True
        
        return False