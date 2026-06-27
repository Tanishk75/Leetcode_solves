class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        ws = 0
        ml = float('inf')

        for r in range(len(nums)):
            ws += nums[r]

            while ws >= target:
                ml = min(ml, r - l + 1)
                ws -= nums[l]
                l += 1

        return 0 if ml == float('inf') else ml