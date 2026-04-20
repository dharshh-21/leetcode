class Solution:
    def rob(self, nums) :
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev2 = 0
        prev1 = 0
        for amount in nums:
            current_max = max(prev1, prev2 + amount)
            prev2 = prev1
            prev1 = current_max
        return prev1
        