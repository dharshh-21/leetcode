class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Check if target is at mid
            if nums[mid] == target:
                return mid
            
            # If target is greater, ignore left half
            elif nums[mid] < target:
                left = mid + 1
            
            # If target is smaller, ignore right half
            else:
                right = mid - 1

        return -1


# Example usage
obj = Solution()
print(obj.search([-1, 0, 3, 5, 9, 12], 9))
        