class Solution:
    def subsets(self, nums):
        results = []
        def backtrack(index, current_subset):
            if index == len(nums):
                results.append(list(current_subset))
                return
            current_subset.append(nums[index])
            backtrack(index + 1, current_subset)
            current_subset.pop()
            backtrack(index + 1, current_subset)
        backtrack(0, [])
        return results
        