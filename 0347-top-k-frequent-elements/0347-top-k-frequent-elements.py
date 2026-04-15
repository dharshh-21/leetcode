class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count frequency
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Step 2: Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        # Step 3: Collect top k elements
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result


# Example usage
obj = Solution()
print(obj.topKFrequent([1, 1, 1, 2, 2, 3], 2))
        