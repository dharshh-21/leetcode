class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}  # To handle subarrays starting from index 0

        for num in nums:
            prefix_sum += num

            # Check if (prefix_sum - k) exists
            if (prefix_sum - k) in prefix_map:
                count += prefix_map[prefix_sum - k]

            # Store current prefix_sum in map
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return count


# Example usage
obj = Solution()
print(obj.subarraySum([1, 1, 1], 2))
        