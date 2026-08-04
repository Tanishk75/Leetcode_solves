class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            mx = curr_max * x
            mi = curr_min * x

            curr_max = max(x, mx, mi)
            curr_min = min(x, mx, mi)

            answer = max(answer, curr_max)

        return answer