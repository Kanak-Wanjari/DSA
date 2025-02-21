class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        max = nums[0]
        sum = 0
        for i in range(n):
            sum += nums[i]
            if max < sum:
                max = sum
            if sum < 0:
                sum = 0
        return max