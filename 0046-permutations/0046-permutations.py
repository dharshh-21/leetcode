class Solution:
    def permute(self, nums):
        res = []
        def backtrack(current_permutation, used_mask):
            if len(current_permutation) == len(nums):
                res.append(list(current_permutation))
                return
            for i in range(len(nums)):
                if used_mask[i]:
                    continue
                used_mask[i] = True
                current_permutation.append(nums[i])
                backtrack(current_permutation, used_mask)
                current_permutation.pop()
                used_mask[i] = False
        backtrack([], [False] * len(nums))
        return res
        