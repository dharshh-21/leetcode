class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # Either take current element or extend previous subarray
            current_sum = max(nums[i], current_sum + nums[i])

            # Update global maximum
            max_sum = max(max_sum, current_sum)

        return max_sum


# Example usage
obj = Solution()
print(obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        